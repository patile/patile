<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/jquery-ui.min.js"></script>
<script>

        function getDistanceFromLatLonInKm(lat1,lon1,lat2,lon2) {
              var R = 6371; // Radius of the earth in km
              var dLat = deg2rad(lat2-lat1);  // deg2rad below
              var dLon = deg2rad(lon2-lon1);
              var a =
                Math.sin(dLat/2) * Math.sin(dLat/2) +
                Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) *
                Math.sin(dLon/2) * Math.sin(dLon/2)
                ;
              var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
              var d = R * c; // Distance in km
              return d;
        }

        function deg2rad(deg) {
          return deg * (Math.PI/180)
        }



           var trHTML = " "

           var ajax_func = function () {
                                $.ajax({
                        type: 'GET',
                        url: '127.0.0.1:8000', // eger data ihbarlarda aranan bulunursa dom'u manuple et.
                        dataType: 'json',
                        success: function (data) {
                                var json = data;
                                obj = JSON.parse(json);
                        $.each(obj,function(i,item){
                            data = getDistanceFromLatLonInKm(12.2323,23.2323,45.2323,34.454);




                            console.log(data) // dom manuplation



                        });
                        
                    }
                });

           }

        setInterval(ajax_func,4000)
</script>



