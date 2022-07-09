import { NavLink } from "react-router-dom";

export function ThanksMenu(props) {
    return (
    <div className="flex flex-col justify-center items-center min-h-screen">
        <div className="items-center text-xl w-32 text-center">
            Thanks for your contribution!
        </div>

        <NavLink className="text-white bg-slate-500 hover:bg-white hover:text-slate-500 border-2 border-slate-500 p-3 rounded-md" to='/participate'>Contribute again</NavLink>
        

    </div>)
}