(function () {
    require.config({
        baseUrl: 'js',
        paths: {
            jquery: 'vendor/jquery/jquery.min'
        }
    });

    require(['jquery'], function ($) {
        $.noConflict();
    });
}).call(this);
