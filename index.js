document.addEventListener("DOMContentLoaded", () => {
    const container = document.getElementById("blog_enteries");
    if (!container) return;

    fetch('https://dreamtonegame.com/Blogs/manifest.txt', { cache: 'no-store' })
        .then(response => {
            if (!response.ok) throw new Error('Failed to fetch manifest');
            return response.json();
        })
        .then(entries => {
            entries.sort((a, b) => parseInt(b.INTERNAL) - parseInt(a.INTERNAL));
            const blogDataByOrder = new Array(entries.length);
            const fetchPromises = entries.map((entry, index) => {
                const blogPath = `https://dreamtonegame.com/Blogs/${entry.INTERNAL}.json`;

                return fetch(blogPath, { cache: 'no-store' })
                    .then(resp => {
                        if (!resp.ok) throw new Error(`Failed to fetch blog ${entry.INTERNAL}`);
                        return resp.json().then(blogData => {
                            blogDataByOrder[index] = { entry, blogData };
                        });
                    })
                    .catch(err => {
                        console.error(`Error loading blog entry ${entry.INTERNAL}:`, err);
                        blogDataByOrder[index] = null;
                    });
            });

            Promise.all(fetchPromises).then(() => {
                blogDataByOrder.forEach(item => {
                    if (!item) return;
                    const { entry, blogData } = item;

                    const blogItem = document.createElement("div");
                    blogItem.className = "blogItem";

                    blogItem.innerHTML = `
                        <div class="blogMeta">
                            <div class="blogNumber">#${entry.ID}</div>
                            <div class="blogDate">${blogData.DATE}</div>
                        </div>
                        <div class="blogContent">
                            <div class="blogTitle"><a href="./blog.html?${entry.INTERNAL}">${blogData.TITLE}</a></div>
                            <div class="blogText">
                                ${blogData.PREVIEW || blogData.CONTENT}
                            </div>
                        </div>
                    `;

                    container.appendChild(blogItem);
                });
            });
        })
        .catch(err => {
            console.error('Failed during blog loading:', err);
        });
});
