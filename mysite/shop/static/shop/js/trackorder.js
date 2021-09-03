console.log('trackorder')
// console.log(document.getElementById('trkoid').innerHTML)
var countbtn=0
let trkoid =document.getElementById('trkoid').innerHTML
if(trkoid!==''){

let item=JSON.parse(document.getElementById('itemstring').innerHTML)

var olpd=document.getElementById('olpd')
var li=''
var totalitemprice=0
item.forEach(element => {
    for(let key in element)
    {
        qty = element[key].qty
        names = element[key].name
        price = element[key].price
        
        li+=`<li class="list-group-item d-flex justify-content-between align-items-start">
        <div class="ms-2 me-auto">
          <div class="fw-bold">${names}</div>
          Qty:${qty}
        </div>
        <span class="badge bg-primary">${price*qty}Rs</span>
        </li>`
        olpd.innerHTML=li
        let p =Number(price)        
        let pr = p*qty
        totalitemprice+=pr
    }
});
document.getElementById('totalpriceitem').innerHTML= `<b> ${totalitemprice} </b>`
// console.log(document.getElementsByClassName('btngrp')[0].children.length)




}
else{
    document.getElementsByClassName('righttrk')[0].setAttribute('class','container my-5 righttrk d-none')
    document.getElementsByClassName('wrongclstrk')[0].setAttribute('class','container my-5 wrongclstrk')
}

showhideorderupdate()
function showhideorderupdate() {
    var Choicess = 'Choices'
   
    // let Choices1 = document.getElementById('').innerText
    let Choices2 = document.getElementById('trkbtn2').innerText
    let Choices3 = document.getElementById('trkbtn3').innerText
    let Choices4 = document.getElementById('trkbtn4').innerText
    let Choices5 = document.getElementById('trkbtn5').innerText
    
    if(Choices2!=Choicess){
        document.getElementById('trkcls2').setAttribute('class','list-group-item list-group-item-action my-1 active')
        countbtn+=1
    }
    if(Choices3!=Choicess){
        document.getElementById('trkcls3').setAttribute('class','list-group-item list-group-item-action my-1 active')
        countbtn+=1
    }
    if(Choices4!=Choicess){
        document.getElementById('trkcls4').setAttribute('class','list-group-item list-group-item-action my-1 active')
        countbtn+=1
    }
    if(Choices5!=Choicess){
        document.getElementById('trkcls5').setAttribute('class','btn btn-success my-1')        
        document.getElementById('trkcls2').setAttribute('class','list-group-item list-group-item-action my-1 d-none')
        document.getElementById('trkcls3').setAttribute('class','list-group-item list-group-item-action my-1 d-none')
        document.getElementById('trkcls4').setAttribute('class','list-group-item list-group-item-action my-1 d-none')
        document.getElementById('trkcls1').setAttribute('class','list-group-item list-group-item-action my-1 d-none')
        document.getElementById('btnpg').style.backgroundColor='#198754'
        countbtn+=1
    }
    
    

    if(countbtn>=1)
    {
        let size = countbtn*25
        
        document.getElementById('btnpg').style.width= `${size}%`
        document.getElementById('sppg').innerHTML = `${size}%`
    }
}
