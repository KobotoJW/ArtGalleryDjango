document.addEventListener("DOMContentLoaded", function() {
    var allContent = document.querySelectorAll('.post-content');
    allContent.forEach(function(content) {
        
        var twoLineHeight = "100px";
        if (content.scrollHeight > parseInt(twoLineHeight)) {
            content.style.maxHeight = twoLineHeight;

            if (!content.nextElementSibling || !content.nextElementSibling.classList.contains('read-more')) {
                var readMoreBtn = document.createElement("button");
                readMoreBtn.innerHTML = "Read More";
                readMoreBtn.classList.add('read-more');
                readMoreBtn.onclick = function() { toggleContent(content.id); };
                content.parentNode.insertBefore(readMoreBtn, content.nextSibling);
            }
        }
    });
});

function toggleContent(contentId) {
    var content = document.getElementById(contentId);
    var readMoreBtn = content.nextElementSibling;
    if (content.classList.contains('expanded')) {
        content.style.maxHeight = "100px";
        content.classList.remove('expanded');
        readMoreBtn.innerHTML = "Read More";
    } else {
        content.style.maxHeight = content.scrollHeight + "px";
        content.classList.add('expanded');
        readMoreBtn.innerHTML = "Show Less";
    }
}


document.addEventListener('DOMContentLoaded', function() {
    const posts = document.querySelectorAll('.post-photos');

    posts.forEach(post => {
        let currentImgIndex = 0;
        const images = post.querySelectorAll('img');
        const nextButton = post.querySelector('.next');
        const prevButton = post.querySelector('.prev');

        if(images.length <= 1) {
            nextButton.style.display = 'none';
            prevButton.style.display = 'none';
        }

        nextButton.addEventListener('click', function() {
            images[currentImgIndex].style.display = 'none';
            currentImgIndex = (currentImgIndex + 1) % images.length;
            images[currentImgIndex].style.display = 'block';
        });

        prevButton.addEventListener('click', function() {
            images[currentImgIndex].style.display = 'none';
            currentImgIndex = (currentImgIndex - 1 + images.length) % images.length;
            images[currentImgIndex].style.display = 'block';
        });
    });
});