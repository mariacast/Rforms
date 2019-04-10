
    function gId(id)
    {   
        return document.getElementById(id);
    }
    
    gId("tab_optnew").ondblclick = remOpt;
    
    function traspaso(){   
        var code = "<tr><td style='display: none;'>0</td><th>"+gId("Campo").value+"</th><td>"+gId("Tipo").value+"</th><td>"+gId("Opciones").value+"</td></tr>";
        gId("tab_optnew").innerHTML += code;
        
    }
    
    function remOpt()
    {
        r = event.target.parentNode;
        r.parentNode.removeChild(r);
    }
    
    function mostrar(){
        if (gId("Tipo").value == "S") {
            gId("Opt").style.display='block';
        } else {
            gId("Opt").style.display='none';
        }
    
    }
    function clear_textbox()
    {
        gId("Campo").value = "";
        gId("Opciones").value = "";
        
    }
    
    function reset() 
    {
        gId("Tipo").selectedIndex = 0; 
}
