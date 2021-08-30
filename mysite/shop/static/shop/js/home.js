console.log('myscript only home working');

function clickbtn() {
    let getcart = document.querySelectorAll('.btncart');
    getcart.forEach(function(element) {
    element.addEventListener('click',addcart)  
        
});
}
clickbtn()

if(localStorage.getItem('cart')==null){
    var cart=[]
}
else{
    cart=JSON.parse(localStorage.getItem('cart'))
    updatecart(cart)
    cartitem(cart)
    
}
var show=0

function addcart() {
    
    let btnid = this.id
   
    document.querySelector(`#${btnid}`);
    

    let idstr= btnid.toString()
    let newidstr = btnid.slice(2).toString()
    let newcart={}  
    
        
    if(newcart[idstr]!= undefined) {
        qty = newcart[idstr].qty+1;   
        }
        else
        {
            qty = 1
            names = document.getElementById(`name${newidstr}`).innerHTML
            price = document.getElementById('price'+newidstr).innerHTML.slice(0,-3)
            newcart[idstr] = {'qty':qty,'name':names,'price':price};
        }
    
    
    cart.push(newcart)
    localStorage.setItem('cart',JSON.stringify(cart))  
    // let navbar = document.getElementById('navcart').innerHTML= Object.keys(cart).length
   
    updatecart(cart)
    
}


// $(document).ready(function(){
//     $('#popcart').popover('hide');  
//     $('#popcart').click(function(){
//         $('#popcart').popover('show');}); 
// });
 







//how to get list(array) in objects
//access list
/*cart.forEach(function(element) {
    //access object 
    for(let key in element){
        console.log(key)
    }
})*/



function updatecart(cart) {
    var sum=0
    
    cart.forEach(function(element,index){
        for(let key in element){       
            let id = key.slice(2)
            sum+=element[key].qty  
            if(element[key].qty<1){
                document.getElementById(`btn${id}`).innerHTML=`
                <button class="btn btn-primary btncart" id="pr${id}">Add Cart</button>
                ` 
                
                clickbtn()
                
                // console.log('key:',key,'ele:',Object.keys(element)[0])
                if(key==Object.keys(element)[0]){
                    cart.splice(index,1)
                    // localStorage.setItem("cart", JSON.stringify(cart));
                    
                    
                }
            }
            else{
                document.getElementById(`btn${id}`).innerHTML=`
                <button class="btn btn-primary minus" id="minus${id}">-</button>
                <span id="val${id}"> ${element[key].qty} </span>   
                <button class="btn btn-primary plus" id="plus${id}">+</button>`
                
                  
                // let mini = document.getElementById(`minus${id}`)
                // mini.addEventListener('click',minus)
                // function minus() {
                //     // console.log(cart[key])
                //     element[key]=element[key]-1
                //     element[key] = Math.max(0, element[key]);
                //     document.getElementById(`val${id}`).innerText=element[key]                
                //     // console.log(cart[key],'click minius')
                //     cartitem(cart)
                    
                    
                
                // }


                // let plu = document.getElementById(`plus${id}`)
                // plu.addEventListener('click',plus)
                // function plus() {
                //     element[key]=element[key]+1
                //     document.getElementById(`val${id}`).innerText=element[key]              
                //     // console.log(cart[key],'click minius')                    
                //     cartitem(cart)
                    
                // }
            }
        }
    
    })
    
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('navcart').innerText = sum
    cartitem(cart)

}


// $(document).ready(function(){
//     $('[data-toggle="popover"]').popover({sanitize: false,html:true});   
//   });
$(function () {
    $('[data-toggle="popover"]').popover({
        delay: {
            show: 100
        },
         html: true,
         sanitize: false,
         
    })
})   


function cartitem(cart) {   
    var popStr = "";        
            popStr = popStr + "<h5> Cart for your items in my shopping cart </h5><div class='mx-2 my-2'>";
            cart.forEach(function(element) {
                for(let key in element){
                    // console.log(key,allitem[key])
                    // let prid=document.querySelector(`#${key}`)
                    let id = key.slice(2)

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
            popStr = popStr + "<a class='btn btn-primary mx-2' href='checkout'>Checkout</a>" 
       
    
    document.querySelector('#popcart').setAttribute('title','You Items')
    document.querySelector('#popcart').setAttribute('data-bs-content',popStr)  
}
// let clr=document.querySelector('#clrbtn')
//     console.log(clr)
function clrbtn() {
    localStorage.removeItem('cart');
    cart.forEach(function(element) {
        for(let key in element){
            // console.log(key,allitem[key])
            // let prid=document.querySelector(`#${key}`)
            let id = key.slice(2)
            document.getElementById(`btn${id}`).innerHTML=`
                <button class="btn btn-primary btncart" id="pr${id}">Add Cart</button>
                `
                clickbtn()
                cartitem(cart)
        }
    })
    
    cart=[]
    updatecart(cart)
    
}


$('.divpr').on('click','button.minus',function(){
    id= this.id.slice(5);    
    cart.forEach(function(element,index){
        for(let key in element){   
            if(key==`pr${id}`){          
                element[key].qty=element[key].qty-1;
                element[key].qty = Math.max(0, element[key].qty);                
                document.getElementById(`val${id}`).innerText=element[key].qty
                updatecart(cart)
            }
        }
    })
})
$('.divpr').on('click','button.plus',function(){
    id= this.id.slice(4);    
    cart.forEach(function(element,index){
        for(let key in element){
            if(key==`pr${id}`){             
                element[key].qty=element[key].qty+1;                
                document.getElementById(`val${id}`).innerText=element[key].qty
                updatecart(cart)
            }
        }
    })
})
    
   
        

    

    



