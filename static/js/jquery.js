$(document).ready(function() {
    $(".rules-btn").click(function() {
        $("#game-rules").toggle('fade', 1000);
    });
    
    $(".game-rules-ok-btn").click(function() {
        $("#game-rules").hide('fade', 1000);
    });
    
    $('#welcome-screen').delay(2000).fadeOut(1500);
    
    $('.display_positive_negative_points').delay(3000).fadeOut(1500);
    
});

