$(document).ready(function () {
  $(".title-1").click(function () {
    $(".block-1").slideToggle(700);
    $(".icon-1").toggleClass("icon_rot");
  });
  $(".title-2").click(function () {
    $(".block-2").slideToggle(700);
    $(".icon-2").toggleClass("icon_rot");
  });
  $(".title-3").click(function () {
    $(".block-3").slideToggle(700);
    $(".icon-3").toggleClass("icon_rot");
  });

  // open button
  $(".open_call").click(function () {
    $(".call, .background").fadeIn(300);
    $("body").addClass("fixed");
  });

  $(".exit, .background").click(function () {
    $(".call, .background").fadeOut(300);
    $("body").removeClass("fixed");
  });

  $(".call__back").click(function () {
    $(".good__resp").fadeOut(300);
    $(".form").fadeIn(300).css("display", "flex");
  });

  // mask phone
  $(".phone, .short-phone").each(function () {
    $(this).mask("+7 (999) 999-99-99");
  });

  // short form
  let shortName = "";
  let shortPhone = "";
  let name = "";
  let phone = "";
  let message = "";
  let city = "";
  let regist = "";
  let email = "";
  let isValid = true;

  $(".short-name").keyup(function () {
    shortName = $(".short-name").val();
    isValid = true;
    $(".short-name").removeClass("error");
  });

  $(".name").keyup(function () {
    name = $(".name").val();
    isValid = true;
    $(".name").removeClass("error");
  });

  $(".short-phone").keyup(function () {
    shortPhone = $(".short-phone").val();
    isValid = true;
    $(".short-phone").removeClass("error");
  });

  $(".phone").keyup(function () {
    phone = $(".phone").val();
    isValid = true;
    $(".phone").removeClass("error");
  });

  $(".email").keyup(function () {
    phone = $(".email").val();
  });

  $(".message").keyup(function () {
    message = $(".message").val();
    isValid = true;
    $(".message").removeClass("error");
  });

  $(".city").keyup(function () {
    city = $(".city").val();
    isValid = true;
    $(".city").removeClass("error");
  });

  $(".regist").keyup(function () {
    regist = $(".regist").val();
    isValid = true;
    $(".regist").removeClass("error");
  });

  $(".submit").click(async function () {
    if (shortName === "") {
      isValid = false;
      $(".short-name").addClass("error");
    }

    if (shortPhone === "") {
      isValid = false;
      $(".short-phone").addClass("error");
    }
    if (message === "") {
      isValid = false;
      $(".message").addClass("error");
    }
    if (isValid) {
      let formData = new FormData();
      formData.append("name", shortName);
      formData.append("phone", shortPhone);
      formData.append("email", email);
      formData.append("message", message);

      let requestOptions = {
        method: "POST",
        body: formData,
      };
      let response = await fetch(
        `https://fl-bankrotstvo.ru/onepage/short/`,
        requestOptions
      );
      if (response.ok) {
        $(".form").fadeOut(300);
        $(".good__resp").fadeIn(300).css("display", "flex");
      }
    }
  });

  let q = false;
  let item = 0;

  $(".questions__btn-next , .head__btn").click(function () {
    q = $("input[name='question-200']:checked").val();
    if (q) {
      $(".head__label").removeClass("error-text");
      $(`.item-${item}`).fadeOut(0);
      item++;
      $(`.item-${item}`).fadeIn(500).css("display", "flex");
    } else {
      $(".head__label").addClass("error-text");
    }
  });

  $(".questions__btn-back").click(function () {
    $(`.item-${item}`).fadeOut(0);
    item--;
    $(`.item-${item}`).fadeIn(500).css("display", "flex");
  });

  let q1 = "";
  let q2 = "";
  let q3 = "";
  let q4 = "";
  let q5 = [];

  $(".questions__btn-submit").click(async function () {
    q1 = $("input[name='question-1']:checked").val();
    q2 = $("input[name='question-2']:checked").val();
    q3 = $("input[name='question-3']:checked").val();
    q4 = $("input[name='question-4']:checked").val();
    $.each($("input[name='question-5']:checked"), function () {
      q5.push($(this).val());
    });
    if (name === "") {
      isValid = false;
      $(".name").addClass("error");
    }
    if (phone === "") {
      isValid = false;
      $(".phone").addClass("error");
    }
    if (city === "") {
      isValid = false;
      $(".city").addClass("error");
    }

    if (regist === "") {
      isValid = false;
      $(".regist").addClass("error");
    }

    if (isValid) {
      let formData = new FormData();
      formData.append("summ", q1);
      formData.append("amount", q2);
      formData.append("income", q3);
      formData.append("pledge", q4);
      formData.append("property", q5);
      formData.append("city", city);
      formData.append("registration_city", regist);
      formData.append("phone_number", phone);
      formData.append("email", email);
      formData.append("name", name);

      let requestOptions = {
        method: "POST",
        body: formData,
      };
      let response = await fetch(
        `https://fl-bankrotstvo.ru/onepage/full/`,
        requestOptions
      );

      if (response.ok) {
        $(`.item-${item}`).fadeOut(1);
        item++;
        $(`.item-${item}`).fadeIn(500).css("display", "flex");
      }
    }
    $(".call__back__qustion").click(function () {
      $(`.item-${item}`).fadeOut(1);
      item = 0;
      $(`.item-${item}`).fadeIn(500);
    });
  });

  $('a[href*="#"]').on("click", function (e) {
    e.preventDefault();

    $("html, body").animate(
      {
        scrollTop: $($(this).attr("href")).offset().top,
      },
      500,
      "linear"
    );
  });

  // advantages

  $(".advantages__item-1").click(function () {
    $(".advantages-3, .advantages-2").fadeOut(0);
    $(".advantages-1").fadeIn(500).css("display", "flex");
    $(this).addClass("focus");
    $(".advantages__item-3 , .advantages__item-2").removeClass("focus");
  });

  $(".advantages__item-2").click(function () {
    $(".advantages-1, .advantages-3").fadeOut(0);
    $(".advantages-2").fadeIn(500).css("display", "flex");
    $(this).addClass("focus");
    $(".advantages__item-1 , .advantages__item-3").removeClass("focus");
  });

  $(".advantages__item-3").click(function () {
    $(".advantages-1, .advantages-2").fadeOut(0);
    $(".advantages-3").fadeIn(500).css("display", "flex");
    $(this).addClass("focus");
    $(".advantages__item-1 , .advantages__item-2").removeClass("focus");
  });

  // slider
  let slide = 1;

  $(".right_review").click(function () {
    $(`.slide-${slide}`).fadeOut(0);
    slide === 4 ? (slide = 1) : slide++;
    $(`.slide-${slide}`).fadeIn(300);
  });
  $(".left_review").click(function () {
    $(`.slide-${slide}`).fadeOut(0);
    slide === 1 ? (slide = 4) : slide--;
    $(`.slide-${slide}`).fadeIn(300);
  });

  // scroll

  $(window).scroll(function () {
    if ($(window).scrollTop() > 300) {
      $(".up").fadeIn(300);
    }
    if ($(window).scrollTop() < 300) {
      $(".up").fadeOut(300);
    }
  });

  // ---
});
