/**
 * Created by Ryan Perkins on 10/14/14.
 */
$('.parallax-window').parallax({imageSrc: '../img/PoolCar.jpg'});

/** hides and reveals text
 */
function display(action, id)
{
if (action == 'show')
{
document.getElementById("explanation"+id).style.display = "block";
document.getElementById("link"+id).href= "javascript:display('hide', "+id+")";
document.getElementById("link"+id).innerHTML = "Close";
}

if (action == 'hide')
{
document.getElementById("explanation"+id).style.display = "none";
document.getElementById("link"+id).href= "javascript:display('show', "+id+")";
document.getElementById("link"+id).innerHTML = "Death to Traffic";
}
}

// Closes the sidebar menu
    $("#menu-close").click(function(e) {
        e.preventDefault();
        $("#sidebar-wrapper").toggleClass("active");
    });

    // Opens the sidebar menu
    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#sidebar-wrapper").toggleClass("active");
    });

    // Scrolls to the selected menu item on the page
    $(function() {
        $('a[href*=#]:not([href=#])').click(function() {
            if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') || location.hostname == this.hostname) {

                var target = $(this.hash);
                target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
                if (target.length) {
                    $('html,body').animate({
                        scrollTop: target.offset().top
                    }, 1000);
                    return false;
                }
            }
        });
    });