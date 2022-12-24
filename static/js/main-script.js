var side_controls_shifter = document.querySelectorAll(
  ".side-controls-shifter svg"
);
var side_control_page_1 = document.querySelectorAll(".side-control-page-1");
var side_control_page_2 = document.querySelectorAll(".side-control-page-2");

var actionButton = document.querySelectorAll(".action-button button");

var hiddenUpload = document.querySelector(".action-button .hidden-upload");

var image_workspaceSpan = document.querySelectorAll(".image-workspace span");

var preview_containerSpan = document.querySelectorAll(
  ".preview-container span"
);

var zoom = document.querySelectorAll(".side-control-page-1 .zoom svg");
// var rotate = document.querySelectorAll(".side-control-page-1 .rotate svg");
var flip = document.querySelectorAll(".side-control-page-1 .flip svg");
// var move = document.querySelectorAll(".side-control-page-1 .move svg");
var aspectRatio = document.querySelectorAll(".side-control-page-2 .aspect li");
var controlCropper = document.querySelectorAll(
  ".bottom-control .ctrl-cropper svg"
);
var lockCropper = document.querySelectorAll(".bottom-control .lock svg");
var dargMode = document.querySelectorAll(".bottom-control .drag-mode svg");

// shift control pages
side_controls_shifter[0].onclick = () => {
  side_control_page_1[0].style.display = "block";
  side_control_page_2[0].style.display = "none";
  side_controls_shifter[0].classList.add("active");
  side_controls_shifter[1].classList.remove("active");
};
side_controls_shifter[1].onclick = () => {
  side_control_page_1[0].style.display = "none";
  side_control_page_2[0].style.display = "block";
  side_controls_shifter[0].classList.remove("active");
  side_controls_shifter[1].classList.add("active");
};
side_controls_shifter[2].onclick = () => {
  side_control_page_1[1].style.display = "block";
  side_control_page_2[1].style.display = "none";
  side_controls_shifter[2].classList.add("active");
  side_controls_shifter[3].classList.remove("active");
};
console.log(side_control_page_1);
side_controls_shifter[3].onclick = () => {
  side_control_page_1[1].style.display = "none";
  side_control_page_2[1].style.display = "block";
  side_controls_shifter[3].classList.add("active");
  side_controls_shifter[2].classList.remove("active");
};

// upload image
let index = 0;
actionButton[0].onclick = () => {
  index = 0;
  hiddenUpload.click();
};
actionButton[2].onclick = function () {
  index = 1;
  hiddenUpload.click();
};
const filesArray = new Array(4);
let c = 0;
hiddenUpload.onchange = async () => {
  // apdate on new file selected issue removed here
  document.querySelectorAll(".image-workspace")[
    index
  ].innerHTML = `<img src="" class="image-${index + 1} alt="">`;
  var image_workspace = document.querySelector(`.image-${index + 1}`);

  var file = hiddenUpload.files[0];
  // console.log(file);
  
  var url = window.URL.createObjectURL(new Blob([file], { type: "image/jpg" }));
  image_workspace.src = url;
  image_workspaceSpan[index].style.display = "none";
  preview_containerSpan[index].style.display = "none";

  var options = {
    // dragMode: "move",
    preview: `.img-preview-${index + 1}`,
    viewMode: 2,
    modal: false,
    background: false,
    ready: function () {
      // zoom for image

      zoom[index * 2].onclick = () => cropper.zoom(0.1);
      zoom[index * 2 + 1].onclick = () => cropper.zoom(-0.1);

      // flip image
      var flipX = -1;
      var flipY = -1;
      flip[0 + index * 2].onclick = () => {
        cropper.scale(flipX, 1);
        flipX = -flipX;
      };
      flip[1 + index * 2].onclick = () => {
        cropper.scale(1, flipY);
        flipY = -flipY;
      };

      // set aspect ratio
      aspectRatio[0 + 5 * index].onclick = () =>
        cropper.setAspectRatio(1.7777777777777777);
      aspectRatio[1 + 5 * index].onclick = () =>
        cropper.setAspectRatio(1.3333333333333333);
      aspectRatio[2 + 5 * index].onclick = () => cropper.setAspectRatio(1);
      aspectRatio[3 + 5 * index].onclick = () =>
        cropper.setAspectRatio(0.6666666666666666);
      aspectRatio[4 + 5 * index].onclick = () => cropper.setAspectRatio(0); // free

      // cropper control
      controlCropper[0 + index * 2].onclick = () => cropper.clear();
      controlCropper[1 + index * 2].onclick = () => cropper.crop();

      // lock cropper
      lockCropper[0 + index * 2].onclick = () => cropper.disable();
      lockCropper[1 + index * 2].onclick = () => cropper.enable();

      // download cropped image
      actionButton[1 + index * 2].onclick = async () => {
        actionButton[1].innerText = "...";
        cropper.getCroppedCanvas().toBlob(async (blob) => {
          var downloadUrl = window.URL.createObjectURL(blob);
          var a = document.createElement("a");
          a.href = downloadUrl;
          const fileName = `${file.name}-cropped`;
          a.download = fileName; // output image name
          a.click();
          actionButton[1].innerText = "Download";
          filesArray[c % 4] = file.name;
          c++;
          filesArray[c % 4] = fileName;
          c++;
        });
      };
    },
  };

  var cropper = await new Cropper(image_workspace, options);
};

const mergebtn = document.querySelector(".merge-btn");
mergebtn.onclick = async function () {
  actionButton[1].click();
  actionButton[3].click();
  setTimeout(() => {
    $.ajax({
      type: "POST",
      url: "/merge",
      data: {
        fImage: filesArray[0],
        fImageCropped: filesArray[1],
        sImage: filesArray[2],
        sImageCropped: filesArray[3],
      },
      async: true,
      success: function (res) {
        console.log(res);
        document
          .querySelector(".merged-image-workspace")
          .insertAdjacentHTML(
            "afterbegin",
            `<img src="/photos/patients1.png" alt="">`
          );
      },
    });
  }, 500);
  // BUG  should send the photos or their name
};
