console.log('Home');

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
    cartitem()
    
}
var show=0

function addcart() {
    
    let btnid = this.id
   
    let parent = document.querySelector(`#${btnid}`);
    // let prname = parent.parentElement.children[0].innerText
    // let prprice = parent.parentElement.children[2].innerText
    // console.log(prname,prprice)

    let idstr= btnid.toString()
    let newcart={}  
    
        
    if(newcart[idstr]!= undefined) {
        
        newcart[idstr] = newcart[idstr]+1;      
        }
        else
        {
        newcart[idstr] = 1;
        }
    
    
    cart.push(newcart)
    localStorage.setItem('cart',JSON.stringify(cart))  
    // let navbar = document.getElementById('navcart').innerHTML= Object.keys(cart).length
   
    updatecart(cart)
    cartitem()
}



function cartitem() {    


allitem = JSON.parse(localStorage.getItem('cart'))

var htmlte=''
allitem.forEach(function(element) {
    for(let key in element){
        // console.log(key,allitem[key])
        // let prid=document.querySelector(`#${key}`)
        let id = key.slice(2)

        let name=document.querySelector(`#name${id}`).innerText
        let price=document.querySelector(`#price${id}`).innerText
        
            htmlte+= `<h6>${name}</h6> 
            <button>-</button>
            <span id='val${id}'> ${element[key]}Qty </span>   
            <button>click</button> <p>${price}</p>`
    }
})
    htmlte = htmlte + "<h2>roma</h2>"
    document.querySelector('#popcart').setAttribute('title','You Items')
    document.querySelector('#popcart').setAttribute('data-bs-content',htmlte)

}
$(document).ready(function(){
    $('#popcart').popover('hide');  
    $('#popcart').click(function(){
        $('#popcart').popover('show');}); 
});





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
            sum = sum+element[key] 
            
            if(element[key]<1){
                document.getElementById(`btn${id}`).innerHTML=`
                <button class="btn btn-primary btncart" id="pr${id}">Add Cart</button>
                ` 
                clickbtn()
                
                // console.log('key:',key,'ele:',Object.keys(element)[0])
                if(key==Object.keys(element)[0]){
                    cart.splice(index,1)
                    // localStorage.setItem("cart", JSON.stringify(cart));
                    updatecart(cart)
                    cartitem()
                }
            }
            else{
                document.getElementById(`btn${id}`).innerHTML=`
                <button class="btn btn-primary minus" id="minus${id}">-</button>
                <span id="val${id}"> ${element[`pr${id}`]} </span>   
                <button class="btn btn-primary plus" id="plus${id}">+</button>`
                
                  
                let mini = document.getElementById(`minus${id}`)
                mini.addEventListener('click',minus)
                function minus() {
                    // console.log(cart[key])
                    element[key]=element[key]-1
                    element[key] = Math.max(0, element[key]);
                    document.getElementById(`val${id}`).innerText=element[key]                
                    // console.log(cart[key],'click minius')
                    updatecart(cart)
                    cartitem()
                
                }


                let plu = document.getElementById(`plus${id}`)
                plu.addEventListener('click',plus)
                function plus() {
                    element[key]=element[key]+1
                    document.getElementById(`val${id}`).innerText=element[key]              
                    // console.log(cart[key],'click minius')
                    updatecart(cart)
                    cartitem()
                }
            }
        }
    
    })
    
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('navcart').innerText = sum


}


 
    
    


    
   
        

    

    



