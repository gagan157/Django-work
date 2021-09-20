console.log('setting')

// $(document).ready(function(){
//     $("#pr").click(function(){
//         $("#profile").addClass('active')
//         $("#pr").addClass('active')

//         $("#account").removeClass('active')
//         $("#security").removeClass('active')
//         $("#notification").removeClass('active')
//         $("#billing").removeClass('active')  

//         $("#ac").removeClass('active')
//         $("#sc").removeClass('active')
//         $("#no").removeClass('active')
//         $("#bi").removeClass('active')

//       });
  
//   });

$(document).ready(function(){
    $("#ac").click(function(){
        $("#account").addClass('active')
        $("#ac").addClass('active')

        $("#profile").removeClass('active')
        $("#security").removeClass('active')
        $("#notification").removeClass('active')
        $("#billing").removeClass('active') 
        
        $("#pr").removeClass('active')
        $("#sc").removeClass('active')
        $("#no").removeClass('active')
        $("#bi").removeClass('active')
      });
  
  });
$(document).ready(function(){
    $("#sc").click(function(){
        $("#security").addClass('active')
        $("#sc").addClass('active')

        $("#profile").removeClass('active')
        $("#account").removeClass('active')
        $("#notification").removeClass('active')
        $("#billing").removeClass('active') 
        
        $("#pr").removeClass('active')
        $("#ac").removeClass('active')
        $("#no").removeClass('active')
        $("#bi").removeClass('active')
      });
  
  });
$(document).ready(function(){
    $("#no").click(function(){
        $("#notification").addClass('active')
        $("#no").addClass('active')

        $("#profile").removeClass('active')
        $("#account").removeClass('active')
        $("#security").removeClass('active')
        $("#billing").removeClass('active') 
        
        $("#pr").removeClass('active')
        $("#ac").removeClass('active')
        $("#sc").removeClass('active')
        $("#bi").removeClass('active')
      });
  
  });
$(document).ready(function(){
    $("#bi").click(function(){
        $("#billing").addClass('active')
        $("#bi").addClass('active')

        $("#profile").removeClass('active')
        $("#account").removeClass('active')
        $("#security").removeClass('active')
        $("#notification").removeClass('active') 
        
        $("#pr").removeClass('active')
        $("#ac").removeClass('active')
        $("#sc").removeClass('active')
        $("#no").removeClass('active')
      });
  
  });
 







