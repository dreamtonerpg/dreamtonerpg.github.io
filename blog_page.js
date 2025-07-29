document.addEventListener('DOMContentLoaded', function () {
    const url = window.location.href;
    const urlObject = new URL(url);
    const queryString = urlObject.search;
    const numberValue = queryString.slice(1);
    comments = true

    console.log(numberValue);
    fetch('https://dreamtonegame.com/Blogs/' + numberValue.toString() + '.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log(data);

            document.getElementById('BLOG_TITLE').innerHTML = "#" + data.ID + ": " + data.TITLE;
            document.getElementById('BLOG_DATE').innerHTML = "- " + data.DATE;
            document.getElementById('BLOG_CONTENT').innerHTML = data.CONTENT;

            document.querySelector('.blog').classList.add('loaded');

        })
        .catch(error => {
            console.error('Error fetching the file:', error);
        });
});
