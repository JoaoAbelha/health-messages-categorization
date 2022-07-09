
import { Navbar } from "./components/navbar"

import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./Home";
import Instructions from "./Instructions";
import { ThanksMenu } from "./ThanksMenu";
import { Footer } from "./Footer";

export default function App() {



  return (
    <BrowserRouter>    
      <Navbar/>
        <div>
          <Routes>
            <Route exact path="/" element={<Instructions/>}/>
            <Route exact path="/participate" element={<Home/>}/>
            <Route path = '/thanks-menu' element={<ThanksMenu/>}></Route>
          </Routes>
        </div>
        <Footer/>
    </BrowserRouter>
  )


}