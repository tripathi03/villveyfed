var show_add_application_modal = () => {
    $("#add-application-modal").show();
}
var hide_add_application_modal = () => {
    $("#add-application-modal").hide();
}
var hideNavbarMessagebarInSeconds = (seconds) => {
    setTimeout(() => $("#navbar-message-bar").hide(), 1000*seconds);
}
var openApplication = (app_path) => {
    var win = window.open(location.origin+"/"+app_path, '_blank');
    if (win) {
        win.focus();
    } else {
        alert('Please allow popups for this website');
    }
}
var showContextMenu = (event, app_id, app_name) => {
    let [x_pos, y_pos] = [event.pageX+2, event.pageY+2];
    $("#application-context-menu").show();
    $("#application-context-menu").attr('appId',$(event.target).attr('appId'));
    $("#application-context-menu").attr('appName',$(event.target).attr('appName'));
    $("#application-context-menu").css("left",x_pos+"px");
    $("#application-context-menu").css("top",y_pos+"px");
}
var deleteApp = (target) => {
    let appId = $("#application-context-menu").attr('appId');
    let appName = $("#application-context-menu").attr('appName');
    $.ajax("/application/delete/"+appId, {
        method: "POST",
        headers: {
            'csrf_token': "{{csrf_token}}"
        },
        success: function(){
            console.log("deleted "+appName);
            location.assign(location.href)
        },
        error: function(){
            console.log("failed to delete "+appName);
        }
    })
}
var viewApp = (target) => {
    let appId = $("#application-context-menu").attr('appId');
    let appName = $("#application-context-menu").attr('appName');
    console.log(appId, appName);
}
var editApp = (target) => {
    let appId = $("#application-context-menu").attr('appId');
    let appName = $("#application-context-menu").attr('appName');
    console.log(appId, appName);
}
var hideApp = (target) => {
    let appId = $("#application-context-menu").attr('appId');
    let appName = $("#application-context-menu").attr('appName');
    console.log(appId, appName);
}

$(document).ready(() => {
    hideNavbarMessagebarInSeconds(5);
    $(document).bind('cut copy', function(event){
        event.preventDefault();
    });
    $(document).on('click', function(event){
        $("#application-context-menu").hide();
    });
    $(".app-item").bind('contextmenu', function(event){
        event.preventDefault();
        let app_id = $(event.target).attr('appId');
        let app_name = $(event.target).attr('appName');
        if(app_id && app_name) {
            showContextMenu(event, app_id, app_name);
        }
    });
    $(".app-item").dblclick(function(event){
        event.preventDefault();
        let app_path = $($(event.target).closest(".application-logo")).attr('appPath');
        if(app_path) openApplication(app_path);
    });
});
