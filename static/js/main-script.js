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
let thirdCounter = 0;
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
  console.log(document.querySelectorAll(".phase-image-workspace"), index);
  document.querySelector(
    `.phase-image-workspace-${index}`
  ).innerHTML = `<img src="" class ="magnitude-img-${index}">`;
  const mag_workspace = document.querySelector(`.magnitude-img-${index}`);
  var file = hiddenUpload.files[0];
  var url = window.URL.createObjectURL(new Blob([file], { type: "image/jpg" }));
  mag_workspace.src = url;
  // sending request for the phase and magnitude
  $.ajax({
    type: "POST",
    url: "/generate",
    data: {
      imgName: file.name,
      required: index,
      counter: imagesCounter,
    },
    async: true,
    success: function (res) {
      document.querySelectorAll(".image-workspace")[
        index
      ].innerHTML = `<img src="" class="image-${index + 1} alt="">`;
      var image_workspace = document.querySelector(`.image-${index + 1}`);

      // BUG here should add the image photo from the response
      image_workspace.src = `./${res}`;
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
              const fileName = `Cropped${thirdCounter}${file.name}`;
              a.download = fileName; // output image name
              a.click();
              actionButton[1].innerText = "Download";
              console.log(index);
              filesArray[c + index * 2] = file.name;
              c++;
              filesArray[c + index * 2] = fileName;
              c = 0;
            });
          };
        },
      };

      var cropper = new Cropper(image_workspace, options);
    },
  });
};

const mergebtn = document.querySelector(".merge-btn");
let imagesCounter = 0;
mergebtn.onclick = async function () {
  index = 0;
  actionButton[1].click();
  setTimeout(() => {
    index = 1;
    actionButton[3].click();
  }, 100);

  setTimeout(() => {
    console.log(filesArray);
    thirdCounter++;
    $.ajax({
      type: "POST",
      url: "/merge",
      data: {
        fImage: filesArray[0],
        fImageCropped: filesArray[1],
        sImage: filesArray[2],
        sImageCropped: filesArray[3],
        counter: imagesCounter,
      },
      async: true,
      success: function (res) {
        console.log(res);
        imagesCounter++;
        document.querySelector(
          ".merged-image-workspace"
        ).innerHTML = `<img src="./${res}" class='gen-image' >`;
      },
    });
  }, 400);
};
