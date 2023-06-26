function openNav(){
            document.getElementById("mySidenav").style.width="250px";
            document.getElementById("myAnalytical").style.marginLeft="250px";
            document.getElementById("myAnalyticalTable").style.width="1100px";
            document.getElementById("myTable2").style.width="676px";
            document.getElementById("myTable3").style.width="1064px";
        }
    
function closeNav(){
            document.getElementById("mySidenav").style.width="0";
            document.getElementById("myAnalytical").style.marginLeft="0";
            document.getElementById("myAnalyticalTable").style.width="1350px";
            document.getElementById("myTable2").style.width="926px";
            document.getElementById("myTable3").style.width="1314px";
        }

$(document).ready(function(){
    //Get references to the dropdown elements
    var dailyDropdown = $('#dailyDropdown');
    var weeklyDropdown= $('#weeklyDropdown');
    var monthlyDropdown= $('#monthlyDropdown');


    //Event handler for daily dropdown change
    $('dailyDropdown').change(function(){
        var selectedOption = $(this).val();
        var graphUrl = $('option:selected',this).data('url');
        updateGraph(graphUrl,'dailyGraphContainer');
    });

    //Event handler for weekly dropdown change
    $('weeklyDropdown').change(function(){
        var selectedOption = $(this).val();
        var graphUrl = $('option:selected',this).data('url');
        updateGraph(graphUrl,'weeklyGraphContainer');
    });

    //Event handler for monthly dropdown change
    $('monthlyDropdown').change(function(){
        var selectedOption = $(this).val();
        var graphUrl = $('option:selected',this).data('url');
        updateGraph(graphUrl,'monthlyGraphContainer');
    });

    //Function to update the graph
    function updateGraph(url,containerId){
        //Perform an AJAX request to fetch the graph data
        $.ajax({
            url:url,
            method:'GET',
            success:function(data){
                //Update the graph using the fetched data
                $('#'+containerId).html(data);
            },
            error:function(){
                //Handle error if necessary
            }
        });
    }
});