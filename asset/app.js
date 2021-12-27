categories = () =>{

     document.getElementById("categories").style.display="block" ;
     document.getElementById("stop").onclick = ()=>{
        document.getElementById("categories").style.display="none" ;
     }

    }
template = ()=>{
   document.getElementById("templates").style.display = "block" ;
   }

stopw = ()=>{
   document.getElementById("templates").style.display = "none" ;
}

form = ()=>{
   document.getElementById("form").style.display = "block" ;
}

AddMore = ()=>{
   
   document.querySelector("#AddHere").insertAdjacentHTML( 'afterbegin' ,`<div>
   
        <input type="text" class="form-control " id="exampleFormControlInput1" placeholder="Project Title">
      <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
      </div>`)

}


