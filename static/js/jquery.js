$(document).ready(function() {
    $(".rules-btn").click(function() {
        $("#game-rules").toggle('fade', 1000);
    });
    
    $(".game-rules-ok-btn").click(function() {
        $("#game-rules").hide('fade', 1000);
    });
    
    
    $("#welcome-screen-button").click(function() {
        $("#welcome-screen").hide('fade', 1000);
    });
});