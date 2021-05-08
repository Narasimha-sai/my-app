import React from "react";

function Footer(){
    const currentdate = new Date();
    const year = currentdate.getFullYear();
    return(
    <footer>
        <p> Copyright ⓒ {year}</p>
    </footer>
    );
}
export default Footer;