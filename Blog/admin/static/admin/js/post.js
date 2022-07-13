const API_URL = 'http://localhost:8000/admin/post';

export default class BlogPost {
    constructor(postID, editor) {
        this.postID = postID;
        this.editor = editor;
        this.editor.onSave.subscribe((ev) => this.savePost(ev));
        this.editor.onPreview.subscribe(this.preview);
    }

    savePost({ event, post }) {
        this.editor.lock();
        this.editor.removeError('title');

        fetch(`${API_URL}/save`, {
            method: 'POST',
            body: JSON.stringify({
                pk: this.postID,
                ...this.editor.getPost()
            })
        })
            .then((res) => res.json())
            .then((res) => {
                if (res.error) {
                    return this.handleResponseError(res.error)
                }

                this.postID = res.pk;
            })
            .catch(console.error)
            .finally(() => {
                this.editor.unlock();
            })
    }

    preview() {
        console.log("previewing post");
    }

    handleResponseError(err) {
        if (err.title) {
            this.editor.showError('title', err.title);
        }
    }
}