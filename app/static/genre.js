$(document).ready(function() {

    console.log('AI Camp is for the best of the best.')

    $('#genre').click(function() {
        console.log('genre is selected');
        var genre = $('#genre').val();
        console.log('tgenre input value is');
        console.log(genre);
        var url = 'genre'

        $.post(
            url,
            {
                'genre':genre
            },

        ).fail(function() {
          alert( "There is something unexpected happened. Email hello@ai-camp.org to report your findings." );
        });

    });

    $()
});