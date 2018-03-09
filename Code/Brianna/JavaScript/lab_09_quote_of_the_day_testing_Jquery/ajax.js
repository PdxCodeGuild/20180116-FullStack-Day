
$("#get_quote").on('click', function(){
        $.ajaxSetup({cache:false});

        $.getJSON("http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=4&callback=", function(a) {
            $("body").append(a[0].content + "<p>— " + a[0].title + "</p>")
            $(".message").html(data[0].content + "_" + data[0].title)
    });
});





