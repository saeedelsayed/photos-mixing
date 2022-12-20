let side_control_page_1 = document.querySelector(".side-control-page-1");
let side_control_page_2 = document.querySelector(".side-control-page-2");
let uploadButton_1 = document.getElementById("upload_1");
let downloadButton_1=document.getElementById('download_1')
console.log(uploadButton_1);
console.log(downloadButton_1);
let hiddenUpload = document.querySelector(".action-button .hidden-upload");
let image_workspaceSpan = document.querySelector(".image-workspace span");
let preview_containerSpan = document.querySelector(".preview-container span");
let zoom = document.querySelectorAll(".side-control-page-1 .zoom svg");
let rotate = document.querySelectorAll(".side-control-page-1 .rotate svg");
let flip = document.querySelectorAll(".side-control-page-1 .flip svg");
let move = document.querySelectorAll(".side-control-page-1 .move svg");
let aspectRatio = document.querySelectorAll(".side-control-page-2 .aspect li");
let controlCropper = document.querySelectorAll(
  ".bottom-control .ctrl-cropper svg"
);
let lockCropper = document.querySelectorAll(".bottom-control .lock svg");
let dargMode = document.querySelectorAll(".bottom-control .drag-mode svg");


// upload image
uploadButton_1.onclick = () => hiddenUpload.click();
hiddenUpload.onchange = () => {
  // apdate on new file selected issue removed here
  document.querySelector(".image-workspace").innerHTML = `<img src="" alt="">`;
  let image_workspace = document.querySelector(".image-workspace img");

  let file = hiddenUpload.files[0];
  let url = window.URL.createObjectURL(new Blob([file], { type: "image/jpg" }));
  image_workspace.src = url;
  image_workspaceSpan.style.display = "none";
  preview_containerSpan.style.display = "none";

  let options = {
    dragMode: "move",
    preview: ".img-preview",
    viewMode: 2,
    modal: false,
    background: false,
    ready: function () {
      // zoom for image
      zoom[0].onclick = () => cropper.zoom(0.1);
      zoom[1].onclick = () => cropper.zoom(-0.1);

      // rotate image
      rotate[0].onclick = () => cropper.rotate(45);
      rotate[1].onclick = () => cropper.rotate(-45);

      // flip image
      let flipX = -1;
      let flipY = -1;
      flip[0].onclick = () => {
        cropper.scale(flipX, 1);
        flipX = -flipX;
      };
      flip[1].onclick = () => {
        cropper.scale(1, flipY);
        flipY = -flipY;
      };

      // move image
      move[0].onclick = () => cropper.move(0, -1);
      move[1].onclick = () => cropper.move(-1, 0);
      move[2].onclick = () => cropper.move(1, 0);
      move[3].onclick = () => cropper.move(0, 1);

      // cropper control
      controlCropper[0].onclick = () => cropper.clear();
      controlCropper[1].onclick = () => cropper.crop();

      // lock cropper
      lockCropper[0].onclick = () => cropper.disable();
      lockCropper[1].onclick = () => cropper.enable();

      // drag mode
      dargMode[0].onclick = () => cropper.setDragMode("crop");
      dargMode[1].onclick = () => cropper.setDragMode("move");

      // download cropped image
      downloadButton_1.onclick = () => {
        downloadButton_1.innerText = "...";
        cropper.getCroppedCanvas().toBlob((blob) => {
          let downloadUrl = window.URL.createObjectURL(blob);
          let a = document.createElement("a");
          a.href = downloadUrl;
          a.download = "cropped-image.jpg"; // output image name
          a.click();
          downloadButton_1.innerText = "Download";
        });
      };
    },
  };

  let cropper = new Cropper(image_workspace, options);
};
