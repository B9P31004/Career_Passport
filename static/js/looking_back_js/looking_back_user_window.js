$(function(){
    var flag=1;
    var user_pk=$('div#user_pk').html();
    $(document).on('click',function(e) {
        if($(e.target).closest('div#Text').length){
            window.location.href = "/looking_back/student_confirm";
        }
        if($(e.target).closest('div#n_11').length){
            window.location.href = "/looking_back/student_confirm";
        }
        if($(e.target).closest('div#n_12').length){
            window.location.href = "/looking_back/student_confirm";
        }
        if($(e.target).closest('div#n_13').length){
            window.location.href = "/looking_back/event/"+user_pk;
        }
        if($(e.target).closest('div#n_14').length){
            window.location.href = "/looking_back/occupational_aptitude/"+user_pk;
        }
        if(!$(e.target).closest('div#n_4__1').length) {
            if(flag==-1){
                $('svg.n_289').hide();
                $('svg.n_290').hide();
                $('div#n__1_1').hide();
                $('div#n__cu').hide();
                $('div#Text_cv').hide();
                $('svg.n_16_cw').hide();
                flag*=-1;
            }
        } else {
            if(flag==1){
                $('svg.n_289').show();
                $('svg.n_290').show();
                $('div#n__1_1').show();
                $('div#n__cu').show();
                $('div#Text_cv').show();
                $('svg.n_16_cw').show();
                flag*=-1;
            }
            else if(flag==-1){
                $('svg.n_289').hide();
                $('svg.n_290').hide();
                $('div#n__1_1').hide();
                $('div#n__cu').hide();
                $('div#Text_cv').hide();
                $('svg.n_16_cw').hide();
                flag*=-1;
            }
        }
     });
});