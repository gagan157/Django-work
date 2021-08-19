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
}
var show=0
function addcart() {
    let btnid = this.id
    // console.log(btnid)
    let parent = document.querySelector(`#${btnid}`);
    let prname = parent.parentElement.children[0].innerText
    let prprice = parent.parentElement.children[2].innerText
    // console.log(prname,prprice)

    let idstr= btnid.toString()

    if(cart[idstr]!= undefined) {
        cart[idstr] = cart[idstr]+1;
       
        }
        else
        {
        cart[idstr] = 1;
        }
    localStorage.setItem('cart',JSON.stringify(cart))  

    
    
}


// function totalItem() {
//     
// }




