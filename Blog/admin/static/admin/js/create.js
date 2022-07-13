import {BlogPostEditor} from './blog-editor.js';
import BlogPost from './post.js';

((global) => {

    const postID = null;
    const container = document.querySelector('.blog-post-container');
    const editor = new BlogPostEditor(container);
    const post = new BlogPost(postID, editor);

    editor.setPost({
        title: "hello",
        keywords: "",
        content: "<b>hi</b>"
    })
})(window);