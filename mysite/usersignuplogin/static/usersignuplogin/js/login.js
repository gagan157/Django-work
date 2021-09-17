console.log('login')



document.getElementById('seepass').addEventListener('click',seepass)
document.getElementById('notseepass').addEventListener('click',notseepass)
document.getElementById('seepass').addEventListener('mouseover',hand)
document.getElementById('notseepass').addEventListener('mouseover',hand2)
// document.getElementsByClassName('pointer').addEventListener('mouseover',hand)

function hand() {
    let seepass=document.getElementById('seepass')
    seepass.style.cursor='pointer'
}
function hand2() {
    let seepass=document.getElementById('notseepass')
    seepass.style.cursor='pointer'
}

function seepass() {
    document.getElementById('notseepass').setAttribute('class','pointer')
    document.getElementById('seepass').setAttribute('class','pointer d-none')
}
function notseepass() {
    document.getElementById('seepass').setAttribute('class','pointer')
    document.getElementById('notseepass').setAttribute('class','pointer d-none')
}