let MovieObject = {
    getall: function(){
        $.ajax({
            type: "GET",
            url: "http://localhost:8000/all/"

        }).done(function(responce){
            console.log(responce.result)
            movielist = responce.result
            console.log(movielist[0].title)

            // topdiv = document.createElement("div")
            // topdiv.style = 'column-count:5'
            // document.body.appendChild(topdiv)
            topdiv = document.getElementById("alldiv")

            movielist.forEach(movie=> {
                cmovie = document.createElement('div')
                cmovie.className = "card"

                mimg = document.createElement("img")
                mimg.className = "card-img-top"
                mimg.src = movie.poster_path
                mimg.onclick = function(){
                    window.location.href = movie.url
                }
                mimg.mouseover = function(){
                    mimg.style.cursor = "pointer";
                }
                mimg.addEventListener("mouseover", function() {
                    mimg.style.cursor = "pointer";
                });

                cmovie.appendChild(mimg)
                topdiv.appendChild(cmovie)
            });
        }).fail();

        },

    getgenres: function(){
        // alert("장르추천")

        genre = document.getElementById("sgenre").value.toLowerCase()
        $.ajax({
            type: "GET",
            url: "http://localhost:8000/genres/" + genre
        }).done(function(responce){
            console.log(responce.result)
            movielist = responce.result
            console.log(movielist[0].title)

            // topdiv = document.createElement("div")
            // topdiv.style = 'column-count:5'
            // document.body.appendChild(topdiv)
            topdiv = document.getElementById("genrediv")
            // topdiv.innerHTML =""
            while(topdiv.firstChild){
                topdiv.removeChild(topdiv.firstChild);
            }
            
            movielist.forEach(movie=> {
                cmovie = document.createElement('div')
                cmovie.className = "card"

                mimg = document.createElement("img")
                mimg.className = "card-img-top"
                mimg.src = movie.poster_path
                mimg.onclick = function(){
                    window.location.href = movie.url
                }
                mimg.mouseover = function(){
                    mimg.style.cursor = "pointer";
                }
                mimg.addEventListener("mouseover", function() {
                    mimg.style.cursor = "pointer";
                });

                cmovie.appendChild(mimg)
                topdiv.appendChild(cmovie)
            }); 
        })
        
    },
    
    getitems: function(){
        // alert("장르추천")

        // genre = document.getElementById("sgenre").value.toLowerCase()
        $.ajax({
            type: "GET",
            url: "http://localhost:8000/item-based/" + "50"
        }).done(function(responce){
            console.log(responce.result)
            movielist = responce.result
            console.log(movielist[0].title)

            topdiv = document.getElementById("itemdiv")
            while(topdiv.firstChild){
                topdiv.removeChild(topdiv.firstChild);
            }
            
            movielist.forEach(movie=> {
                cmovie = document.createElement('div')
                cmovie.className = "card"

                mimg = document.createElement("img")
                mimg.className = "card-img-top"
                mimg.src = movie.poster_path
                mimg.onclick = function(){
                    window.location.href = movie.url
                }
                mimg.mouseover = function(){
                    mimg.style.cursor = "pointer";
                }
                mimg.addEventListener("mouseover", function() {
                    mimg.style.cursor = "pointer";
                });

                cmovie.appendChild(mimg)
                topdiv.appendChild(cmovie)
            }); 
        })
        
    },

    getusers: function(){
        // alert("장르추천")

        // genre = document.getElementById("sgenre").value.toLowerCase()
        $.ajax({
            type: "GET",
            url: "http://localhost:8000/user-based/?"  + "params=50:5"
        }).done(function(responce){
            console.log(responce.result)
            movielist = responce.result
            console.log(movielist[0].title)

            topdiv = document.getElementById("userdiv")
            while(topdiv.firstChild){
                topdiv.removeChild(topdiv.firstChild);
            }
            
            movielist.forEach(movie=> {
                cmovie = document.createElement('div')
                cmovie.className = "card"

                mimg = document.createElement("img")
                mimg.className = "card-img-top"
                mimg.src = movie.poster_path
                mimg.onclick = function(){
                    window.location.href = movie.url
                }
                mimg.mouseover = function(){
                    mimg.style.cursor = "pointer";
                }
                mimg.addEventListener("mouseover", function() {
                    mimg.style.cursor = "pointer";
                });

                cmovie.appendChild(mimg)
                topdiv.appendChild(cmovie)
            }); 
        })
        
    },
}

MovieObject.getall()