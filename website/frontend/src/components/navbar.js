import { NavLink } from "react-router-dom";

export function Navbar(props) {
    return (
    <div className="sticky top-0 w-full">
        
    <nav className="flex p-4 bg-[#8C2D19]">
        <ul className="flex gap-4 mx-3">
            <NavLink  style={({ isActive }) => ({
              color: isActive ? '#fff' : '#BBB'
            })} to = "/participate">Participate</NavLink> | {" "}
            <NavLink target="_blank"  style={({ isActive }) => ({
              color: isActive ? '#fff' : '#BBB',
            })} to = "/">Instructions</NavLink>
        </ul>
    </nav> 
    </div>
);
}