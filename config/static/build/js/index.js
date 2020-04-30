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
    console.log(shortName);
    isValid = true;
    $(".short-name").removeClass("error");
  });

  $(".name").keyup(function () {
    name = $(".name").val();
    console.log(name);
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
    console.log(message);
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
      console.log(shortName);
    }

    if (shortPhone === "") {
      isValid = false;
      $(".short-phone").addClass("error");
    }
    if (message === "") {
      isValid = false;
      $(".message").addClass("error");
    }
    console.log(isValid);
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
        `http://77.244.65.15:9000/onepage/short/`,
        requestOptions
      );
      console.log(response);
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
      console.log(name);
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
        `http://77.244.65.15:9000/onepage/full/`,
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

  let notKwiz = true;
  $(window).scroll(function () {
    if (notKwiz) {
      if ($(window).scrollTop() > 700) {
        $(".kwiz").fadeIn(300).css("display", "flex");
      }
    }
  });
  $(".kwiz_exit").click(function () {
    $(".kwiz").fadeOut(300);
    notKwiz = false;
  });

  // ---
});
