var playhouseElements = document.querySelectorAll('.audioplayer-playpause');

playhouseElements.forEach(function(playhouse) {
    playhouse.addEventListener('click', function() {
        var songId = playhouse.parentElement.parentElement.id;
        // console.log('Clicked on song with ID:', songId);

        let last_played_songs = localStorage.getItem("last_played_songs");
        let lps_list;
        if (last_played_songs === null){
            lps_list = []
        } else {
            lps_list = JSON.parse(last_played_songs);
        }

        if (lps_list.length >= 5) {
            while (lps_list.length > 4) {
                lps_list.pop();
            }
        }

        let index = lps_list.indexOf(songId);
        if (index !== -1){
            lps_list.splice(index, 1)
        }
        lps_list.unshift(songId);

        let lps_new = JSON.stringify(lps_list);
        localStorage.setItem("last_played_songs", lps_new);
    });
});