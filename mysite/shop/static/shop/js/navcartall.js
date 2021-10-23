console.log('lol')
$(function () {
    $('[data-toggle="popover"]').popover({
        delay: {
            show: 100
        },
         html: true,
         sanitize: false,
         
    })
})   
if(localStorage.getItem('cart')==null){
    var cart=[]
}
else{
    cart=JSON.parse(localStorage.getItem('cart'))
    navitem(cart)
  
    
}

// console.log(crt)

// crt.forEach(function(element) {
//     for (k in element){
//        pname=element[k].name
//        pqty=element[k].qty
//        pprice=element[k].price
//        console.log(pname,pqty,pprice)
//     }
// })

function navitem(crt) {   
    var popStr = "";        
            popStr = popStr + "<h5> Cart for your items in my shopping cart </h5><div class='mx-2 my-2'>";
            var count=0
            crt.forEach(function(element) {
                
                for(let key in element){
                    // console.log(key,allitem[key])
                    // let prid=document.querySelector(`#${key}`)
                    let id = key.slice(2)
                    count+=element[key].qty
                    let price = element[key].price
                    let totalprice = Number(price)
                        popStr = popStr + `<h6><h5>${element[key].name}</h5>
                        <span id="btn${id}" class="divpr">
                        <button class="btn btn-primary minus" id="minus${id}">-</button>
                        <span id="val${id}"> ${element[key].qty} </span>   
                        <button class="btn btn-primary plus" id="plus${id}">+</button>
                        </span>                   
                        ${totalprice*element[key].qty}Rps.</h6>`

                    
                }
            })
            popStr = popStr + "</div>" 
            popStr = popStr + "<button class='btn btn-primary' id='clrbtn' onClick='clrbtn()'>Clear</button>"
            popStr = popStr + "<a class='btn btn-primary mx-2' href='/shop/checkout'>Checkout</a>" 
       
    document.getElementById('navcart').innerHTML=count
    document.querySelector('#popcart').setAttribute('title','You Items')
    document.querySelector('#popcart').setAttribute('data-bs-content',popStr)  
}

