console.log("checkout");
var cartdata = JSON.parse(localStorage.getItem("cart"));

var items = "";
// console.log(cartdata == null)
if (cartdata.length !== 0) {
  document.getElementById("yourcart").innerHTML = cartdata.length;
  checkoutcart(cartdata)
} 
else {
  document.getElementById("yourcart").innerHTML = 0;
  items += `
  <li class="list-group-item d-flex justify-content-between bg-light">
    <div class="text-success">
      <h6 class="my-0">No Item</h6>
    </div>
  </li>
  `;
  $("#checkoutul").append(items);
}


function checkoutcart(cartdata) {
  var ctotalprice = 0;
  cartdata.forEach(function (element) {
    for (let key in element) {
      items += ` <li class="list-group-item d-flex justify-content-between lh-sm">
        <div>
          <h6 class="my-0">${element[key].name}</h6>
          <small class="text-muted">Brief description</small>
        </div>
        <div>
          <h6 class="my-0">${element[key].qty}</h6>
        </div>
        <span class="text-muted">${element[key].price * element[key].qty}</span>
        </li> `;
      let pri = Number(element[key].price);
      let qut = pri * element[key].qty;
      ctotalprice += qut;
    }
  });

    items += `
  <li class="list-group-item d-flex justify-content-between bg-light">
    <div class="text-success">
      <h6 class="my-0">Promo code</h6>
      <small>EXAMPLECODE</small>
    </div>
    <span class="text-success">−$5</span>
  </li>
  <li class="list-group-item d-flex justify-content-between">
    <span>Total (USD)</span>
    <strong>$${ctotalprice}</strong>
  </li>`;
  $("#checkoutul").append(items);

 senditem(cartdata)
// $('#itemjson').val(JSON.stringify( localStorage.getItem('cart')));
}


function senditem(cartdata) {

  
  document.getElementById('itemjson').value= JSON.stringify(cartdata)
  
}

