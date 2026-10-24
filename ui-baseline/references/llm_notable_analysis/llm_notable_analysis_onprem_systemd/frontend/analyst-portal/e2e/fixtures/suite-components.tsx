import {useState} from "react";
import {createRoot} from "react-dom/client";
import {Button} from "../../src/components/ui/button";
import {Input} from "../../src/components/ui/input";
import {Textarea} from "../../src/components/ui/textarea";
import {NativeSelect} from "../../src/components/ui/native-select";
import {Badge} from "../../src/components/ui/badge";
import {ConfirmDialog} from "../../src/components/ui/confirm-dialog";
import {Select,SelectTrigger,SelectValue,SelectContent,SelectItem} from "../../src/components/ui/select";
import {Tabs,TabsList,TabsTrigger,TabsContent} from "../../src/components/ui/tabs";
import "./suite-components-context.css";
import "../../src/suite-workspace.css";
function Fixture(){
 const [open,setOpen]=useState(false),[busy,setBusy]=useState(false),[error,setError]=useState<string|null>(null),[attempts,setAttempts]=useState(0);
 function submit(){if(busy)return;setBusy(true);setError(null);setAttempts(n=>n+1);window.addEventListener("suite:complete-request",()=>{setBusy(false);if(attempts===0)setError("Request failed. Retry the action.");else setOpen(false);},{once:true});}
 return <main className="workspace-typography vs-guided-app vs-desk-app vs-unified-app" style={{boxSizing:"border-box",width:"100%",padding:32,maxWidth:1000,margin:"auto"}}>
 <h1 style={{margin:"0 0 16px"}}>Shared component conformance</h1><p style={{margin:"0 0 16px"}}>Isolated component fixture; simulated request failures. No backend or identity claims.</p>
 <section aria-label="Button variants" style={{display:"flex",gap:12,flexWrap:"wrap",margin:"24px 0"}}>
 <Button data-testid="primary">Primary action</Button><Button variant="outline" data-testid="secondary">Secondary action</Button><Button variant="ghost" data-testid="ghost">Text action</Button><Button variant="destructive" data-testid="danger">Delete item</Button><Button disabled data-testid="disabled">Disabled action</Button>
 </section>
 <section aria-label="Fields" style={{display:"grid",gap:16,gridTemplateColumns:"repeat(auto-fit,minmax(220px,1fr))"}}>
 <label>Default field<Input data-testid="field" defaultValue="Entered text" required/></label>
 <label>Read only<Input data-testid="readonly" readOnly value="Saved value"/></label>
 <label>Disabled field<Input disabled value="Unavailable"/></label>
 <label>Invalid field<Input aria-invalid="true" aria-describedby="field-error" defaultValue="Invalid value"/><span id="field-error">Enter a valid value.</span></label>
 <label>Notes<Textarea defaultValue="Multiline content" rows={3}/></label>
 <label>Native choice<NativeSelect defaultValue="one"><option value="one">One</option><option value="two">Two</option></NativeSelect></label>
 <label id="choice-label">Popup choice<Select defaultValue="one"><SelectTrigger aria-labelledby="choice-label"><SelectValue/></SelectTrigger><SelectContent><SelectItem value="one">One</SelectItem><SelectItem value="two">Two</SelectItem></SelectContent></Select></label>
 </section>
 <section aria-label="Badge variants" style={{display:"flex",gap:12,margin:"24px 0",flexWrap:"wrap"}}><Badge data-testid="badge">Information</Badge><Badge variant="warning">Needs review</Badge><Badge variant="success">Complete</Badge><Badge variant="destructive">Failed</Badge><Badge variant="warning" dot>Dot status</Badge></section>
 <Tabs defaultValue="one"><TabsList aria-label="Example views"><TabsTrigger value="one">First view</TabsTrigger><TabsTrigger value="two">Second view</TabsTrigger></TabsList><TabsContent value="one">First view content</TabsContent><TabsContent value="two">Second view content</TabsContent></Tabs>
 <Button style={{marginTop:24}} onClick={()=>{setError(null);setAttempts(0);setOpen(true);}}>Open confirmation</Button><output className="suite-sr-only" aria-label="Request count">{attempts}</output>
 <ConfirmDialog open={open} title="Delete example item?" description="This fixture checks keyboard focus, failure recovery and duplicate submission." confirmLabel="Delete item" confirmingLabel="Deleting item…" confirming={busy} error={error} onConfirm={submit} onCancel={()=>setOpen(false)}/>
 </main>;
}
createRoot(document.getElementById("root")!).render(<Fixture/>);
