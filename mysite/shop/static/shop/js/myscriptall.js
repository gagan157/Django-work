console.log('Working add cart');

let getcart = document.querySelectorAll('.btncart');
getcart.forEach(function(element) {
    element.addEventListener('click',addcart)
   
    
        
});

if(localStorage.getItem('cart')==null){
    var cart={}
}
else{
    cart=JSON.parse(localStorage.getItem('cart'))
    let navbar = document.getElementById('navcart').innerHTML= Object.keys(cart).length
    updatecart(cart)
}
var show=0
function addcart() {
    let btnid = this.id
    // console.log(btnid)
    let parent = document.querySelector(`#${btnid}`);
    // let prname = parent.parentElement.children[0].innerText
    // let prprice = parent.parentElement.children[2].innerText
    // console.log(prname,prprice)

    let idstr= btnid.toString()
    
    if(cart[idstr]!= undefined) {
        cart[idstr] = cart[idstr]+1;
       
        }
        else
        {
        cart[idstr] = 1;
        }
    // localStorage.setItem('cart',JSON.stringify(cart))  
    // let navbar = document.getElementById('navcart').innerHTML= Object.keys(cart).length
    updatecart(cart)
}


var html=''
allitem = JSON.parse(localStorage.getItem('cart'))
for(let key in allitem){
    // console.log(key,allitem[key])
    let prid=document.querySelector(`#${key}`)
    // let prname=prid.parentElement.children[0].innerText
    // let prprice = prid.parentElement.children[2].innerText
    // console.log(prname,allitem[key],prprice)
    if(html !== 'undefined'){
        html+=`<li>${allitem[key]}</li>`
    }
    else{
        html='No Item'
    }
   
    
}
    document.querySelector('#popcart').setAttribute('title','You Items')
    document.querySelector('#popcart').setAttribute('data-bs-content',`${html}`)
    var popover = new bootstrap.Popover(document.querySelector('#popcart'), {
        html: true,
        container: 'body',
    })
  


function updatecart(cart) {
    for(let key in cart){
        let id = key.slice(2)
        if(cart[key]<1){
            document.getElementById(`btn${id}`).innerHTML=`
            <button class="btn btn-primary btncart" id="pr${id}">Add Cart</button>
            ` 
            
        }
        else{
        
        // console.log(id)
        document.getElementById(`btn${id}`).innerHTML=`
        <button class="btn btn-primary minus" id="minus${id}">-</button>
        <span id="val${id}"> ${cart[key]} </span>   
        <button class="btn btn-primary plus" id="plus${id}">+</button>`

             
        let mini = document.getElementById(`minus${id}`)
        mini.addEventListener('click',minus)
        function minus() {
            // console.log(cart[key])
            cart[key]=cart[key]-1
            cart[key] = Math.max(0, cart[key]);
            document.getElementById(`val${id}`).innerText=cart[key]                
            // console.log(cart[key],'click minius')
            updatecart(cart)
           
        }


        let plu = document.getElementById(`plus${id}`)
        plu.addEventListener('click',plus)
        function plus() {
            cart[key]=cart[key]+1
            document.getElementById(`val${id}`).innerText=cart[key]                
            // console.log(cart[key],'click minius')
            updatecart(cart)
        }
        
    }
}
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('navcart').innerHTML= Object.keys(cart).length


}


    let items = JSON.parse(localStorage.getItem('cart'))
    
    for (const [key, value] of Object.entries(items)) {
        console.log(`${key}: ${value}`);
      }
      
  
    
   
        // cart.splice(index, 1);
        // localStorage.setItem('cart', JSON.stringify(cart));
    
    


    
   
        

    

    



