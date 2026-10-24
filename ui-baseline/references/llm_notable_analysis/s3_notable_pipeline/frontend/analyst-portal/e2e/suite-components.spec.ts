import {test,expect,type Page} from "@playwright/test";
import {readFileSync} from "node:fs";
const expectedStyles=JSON.parse(readFileSync(new URL("./fixtures/suite-component-styles.json",import.meta.url),"utf8"));
async function measure(page:Page,selectors:Record<string,string>){return page.evaluate(selectors=>{
 const props=['height','min-height','border-radius','font-family','font-size','font-weight','line-height','background-color','color','border-color','border-width','padding','max-width'];
 return Object.fromEntries(Object.entries(selectors).map(([key,selector])=>{const style=getComputedStyle(document.querySelector(selector)!);return[key,Object.fromEntries(props.map(property=>[property,style.getPropertyValue(property)]))];}));
},selectors);}
test.beforeEach(async({page},testInfo)=>{test.skip(testInfo.config.metadata.suiteComponents!==true,'Run npm run test:components with the dedicated Vite fixture server.');await page.goto('/e2e/fixtures/suite-components.html');await expect(page.getByRole('heading',{name:'Shared component conformance'})).toBeVisible();await page.evaluate(()=>document.fonts.ready);});
test('shared defaults, hover, focus and field boundaries',async({page},testInfo)=>{
 const metrics=await measure(page,{primary:'[data-testid=primary]',secondary:'[data-testid=secondary]',ghost:'[data-testid=ghost]',danger:'[data-testid=danger]',field:'[data-testid=field]',badge:'[data-testid=badge]',textarea:'.suite-textarea',nativeSelect:'select.suite-native-select',popupSelect:'button.suite-select-trigger'});
 expect(metrics).toEqual(expectedStyles[String(testInfo.project.use.browserName)].controls);
 await page.getByTestId('secondary').hover();await expect(page.getByTestId('secondary')).toHaveCSS('background-color','rgb(35, 54, 79)');
 await page.getByTestId('primary').focus();await page.keyboard.press('Tab');await expect(page.getByTestId('secondary')).toBeFocused();await expect(page.getByTestId('secondary')).toHaveCSS('outline-width','2px');
 await expect(page.getByTestId('disabled')).toBeDisabled();await expect(page.getByTestId('readonly')).toHaveAttribute('readonly','');await expect(page.getByTestId('field')).toHaveAttribute('required','');
 await testInfo.attach('computed-components',{body:JSON.stringify(metrics),contentType:'application/json'});
 await page.screenshot({path:testInfo.outputPath('components.png'),fullPage:true});
});
test('confirmation traps focus, restores focus, guards duplicate submission and recovers from failure',async({page},testInfo)=>{
 const opener=page.getByRole('button',{name:'Open confirmation'});await opener.click();const dialog=page.getByRole('alertdialog',{name:'Delete example item?'});await expect(dialog).toBeVisible();await expect(dialog).toHaveAttribute('aria-modal','true');await expect(dialog.getByRole('button',{name:'Cancel'})).toBeFocused();
 expect(await measure(page,{dialog:'[data-suite-component=dialog]',dialogTitle:'.suite-dialog-title',dialogAction:'.suite-dialog-actions button'})).toEqual(expectedStyles[String(testInfo.project.use.browserName)].dialog);
 await page.keyboard.press('Shift+Tab');await expect(dialog.getByRole('button',{name:'Delete item'})).toBeFocused();await page.keyboard.press('Tab');await expect(dialog.getByRole('button',{name:'Cancel'})).toBeFocused();
 await page.keyboard.press('Escape');await expect(dialog).toHaveCount(0);await expect(opener).toBeFocused();await opener.click();await dialog.getByRole('button',{name:'Delete item'}).click();
 await expect(dialog.getByRole('button',{name:'Deleting item…'})).toBeDisabled();await expect(dialog.getByRole('button',{name:'Cancel'})).toBeDisabled();await expect(dialog.getByRole('status')).toHaveText('Deleting item…');await page.keyboard.press('Enter');await page.keyboard.press('Escape');await page.keyboard.press('Tab');expect(await dialog.evaluate(el=>el.contains(document.activeElement))).toBe(true);await expect(dialog).toBeVisible();
 await page.evaluate(()=>window.dispatchEvent(new Event('suite:complete-request')));await expect(dialog.getByRole('alert')).toHaveText('Request failed. Retry the action.');
 await expect(page.locator('output')).toHaveText('1');await dialog.getByRole('button',{name:'Delete item'}).click();await page.evaluate(()=>window.dispatchEvent(new Event('suite:complete-request')));await expect(dialog).toHaveCount(0);await expect(page.locator('output')).toHaveText('2');await expect(opener).toBeFocused();
});
test('popup and tabs retain keyboard behavior',async({page})=>{
 const popup=page.getByRole('combobox',{name:'Popup choice'});await popup.focus();await page.keyboard.press('Enter');await expect(page.getByRole('option',{name:'One',exact:true})).toBeFocused();await page.keyboard.press('ArrowDown');await expect(page.getByRole('option',{name:'Two',exact:true})).toBeFocused();await page.keyboard.press('Enter');await expect(popup).toHaveText('Two');await expect(popup).toBeFocused();
 await page.getByRole('tab',{name:'First view'}).focus();await page.keyboard.press('ArrowRight');await expect(page.getByRole('tab',{name:'Second view'})).toBeFocused();await expect(page.getByRole('tabpanel')).toHaveText('Second view content');
});
test('constrained desktop dialog and enlarged content stay reachable',async({page})=>{
 await page.setViewportSize({width:640,height:480});await page.evaluate(()=>document.documentElement.style.fontSize='32px');await page.getByRole('button',{name:'Open confirmation'}).click();const d=page.getByRole('alertdialog');await expect(d).toBeVisible();const box=await d.boundingBox();expect(box!.x).toBeGreaterThanOrEqual(0);expect(box!.x+box!.width).toBeLessThanOrEqual(640);expect(box!.y+box!.height).toBeLessThanOrEqual(480);for(const b of await d.getByRole('button').all()){await b.scrollIntoViewIfNeeded();await expect(b).toBeInViewport();}await page.keyboard.press('Escape');
});
test('reduced motion retains controls and removes transitions',async({page})=>{await page.emulateMedia({reducedMotion:'reduce'});await expect(page.getByTestId('primary')).toHaveCSS('transition-duration','0s');});
