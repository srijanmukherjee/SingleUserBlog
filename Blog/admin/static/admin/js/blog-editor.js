const { Subject } = rxjs;


const EDITOR_TOOLBAR_OPTIONS = [
    ['bold', 'italic', 'underline', 'strike'],
    ['blockquote', 'code-block'],
    [{'header': 1}, {'header': 2}],
    [{'list': 'ordered'}, {'list': 'bullet'}],
    [{'script': 'sub'}, {'script': 'super'}],
    [{'indent': '-1'}, {'indent': '+1'}],
    [{'direction': 'rtl'}],
    [{'size': ['small', false, 'large', 'huge']}],
    [{'header': [1, 2, 3, 4, 5, 6, false]}],
    [{'color': []}, {'background': []}],
    [{'font': []}],
    [{'align': []}],
    ['link', 'image'],
    ['code-block'],
    ['clean']
];

const EDITOR_OPTIONS = {
    theme: 'snow',
    modules: {
        syntax: true,
        toolbar: EDITOR_TOOLBAR_OPTIONS
    }
}

export class BlogPostEditor {
    constructor(container) {
        this.container = container;
        this.saveBtn = this.container.querySelector("#save-post");
        this.previewBtn = this.container.querySelector("#preview-post");
        this.publishBtn = this.container.querySelector("#publish-post");
        this.titleInput = this.container.querySelector("#blog-title");
        this.keywordsInput = this.container.querySelector("#keywords");
        this.editorContainer = this.container.querySelector("#editor");
        this.titleInputError = this.container.querySelector(".title-input-error");
        this.editor = null;
        this.initializeHljs();
        this.initializeEditor();
        this.bindEvents();

        this.titleInput.value = "";
        this.keywordsInput.value = "";
        this.onSave = new Subject();
        this.onPreview = new Subject();
    }

    initializeHljs() {
        hljs.configure({
            languages: ['javascript', 'ruby', 'python']
        });
    }

    initializeEditor() {
        this.editor = new Quill(this.editorContainer, EDITOR_OPTIONS);
    }

    bindEvents() {
        this.editor.on('text-change', (delta, oldDelta, source) => {
            this.updateState();
        });

        this.titleInput.addEventListener('keyup', () => this.updateState());
        this.keywordsInput.addEventListener('keyup', () => this.updateState());

        this.saveBtn.addEventListener('click', (event) => {
            this.onSave.next({ event, post: this.getPost() });
        })
    }

    // update the states of the button depending on the content
    updateState() {
        this.saveBtn.disabled = true;
        this.previewBtn.disabled = true;
        this.publishBtn.disabled = true;

        const editorHasContent = this.editor.getContents().ops.length > 1 ||
                                 this.editor.getContents().ops[0].insert.trim() != "";

        const shouldSave = editorHasContent ||
                           this.titleInput.value.trim() != "" ||
                           this.keywordsInput.value.trim() != "";

        const shouldPublishAndPreview = editorHasContent &&
                                        this.titleInput.value.trim() != "";

        this.saveBtn.disabled = !shouldSave;
        this.publishBtn.disabled = !shouldPublishAndPreview;
        this.previewBtn.disabled = !shouldPublishAndPreview;
    }

    getPost() {
        return {
            title: this.titleInput.value,
            keywords: this.keywordsInput.value,
            content: this.editor.root.innerHTML
        }
    }

    setPost(post) {
        const { title, keywords, content } = post;

        this.titleInput.value = title ?? "";
        this.keywordsInput.value = keywords ?? "";
        this.editor.clipboard.dangerouslyPasteHTML(content ?? "");
    }

    showError(type, msg) {
        if (type === "title") {
            this.titleInputError.innerText = msg;
            this.titleInputError.classList.remove("uk-hidden");
            this.titleInput.classList.add("uk-form-danger");
        }
    }

    removeError(type) {
        if (type === "title") {
            this.titleInput.classList.remove("uk-form-danger");
            this.titleInputError.classList.add("uk-hidden");
        }
    }

    lock() {
        this.editor.disable();
        this.saveBtn.disabled = true;
        this.publishBtn.disabled = true;
        this.previewBtn.disabled = true;
        this.titleInput.disabled = true;
        this.keywordsInput.disabled = true;
    }

    unlock() {
        this.editor.enable();
        this.updateState();
        this.titleInput.disabled = false;
        this.keywordsInput.disabled = false;
    }
}