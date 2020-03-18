$("#submit").click(function(){
name=$("#name").val();
email=$("#email").val();
message=$("#message").val();
if(name=="" || email=="" || message== "")
    return;

url="http://127.0.0.1:5000"
     $.ajax({
            url: url + "/verify",
            method: "POST",
            cors: true ,
            data: {
                message: message,
            },
            success: function (res) {
             console.log(res);
             if(res.code==1){
             $("#result").append(`<div class="alert alert-danger alert-dismissible fade show" role="alert">
             <strong>Hey! ${name}</strong> You send a ${res.data}
             <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                 <span aria-hidden="true">&times;</span>
             </button>
         </div>`)
        }
         else{
            $("#result").append(`<div class="alert alert-success alert-dismissible fade show" role="alert">
            <strong>Hey! ${name}</strong> You send a ${res.data}
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
         </div>`)
         }
            },
            error: function (err) {
                console.log(err);
                alert(err);
            }
        });
    })