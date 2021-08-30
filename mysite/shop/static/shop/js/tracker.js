console.log('tracker')

console.log(document.getElementsByClassName('trackerclass')[0])
function show() {
    if(document.getElementById('trackerid').innerHTML!==''){
        let heder=document.getElementsByClassName('trackerclass')[0]
        // heder.style.display='inline-block';
        heder.setAttribute('class','trackerclass inline-block')
    }
    
}
show()