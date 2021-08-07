console.log('heloo')
function countWord() {
    let tex = document.getElementById('msgdata').value;
    var count=0
    var split = tex.split('');
    for (var i = 0; i < split.length; i++) {
        if (split[i] != "") {
                    count += 1;
                    
                }
            
    }    
     
   let chcount = document.querySelector('span#count');
   chcount.innerHTML=count
   
   console.log(chcount)
   
}