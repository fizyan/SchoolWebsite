document.addEventListener("DOMContentLoaded", function () {

    const header = document.getElementById("mainHeader");

    function updateHeader() {

        if (!header) return;

        if (window.scrollY > 60) {
            header.classList.add("scrolled");
        } else {
            header.classList.remove("scrolled");
        }

    }

    updateHeader();

    window.addEventListener("scroll", updateHeader);


    /* ================= MOBILE MENU ================= */

    const menuButton =
        document.getElementById("mobileMenuBtn");

    const navMenu =
        document.getElementById("navMenu");


    if (menuButton && navMenu) {

        menuButton.addEventListener("click", function () {

            navMenu.classList.toggle("open");

        });


        navMenu.querySelectorAll("a").forEach(function (link) {

            link.addEventListener("click", function () {

                navMenu.classList.remove("open");

            });

        });

    }


    /* ================= IMAGE REVEAL ================= */

    const images =
        document.querySelectorAll("img");


    const observer =
        new IntersectionObserver(function (entries) {

            entries.forEach(function (entry) {

                if (entry.isIntersecting) {

                    entry.target.classList.add("loaded");

                    observer.unobserve(entry.target);

                }

            });

        }, {
            threshold: 0.1
        });


    images.forEach(function (image) {

        observer.observe(image);

    });

});