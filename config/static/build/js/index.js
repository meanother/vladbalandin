$(document).ready(function () {
  $(".title-1").click(function () {
    $(".block-1").slideToggle(700), $(".icon-1").toggleClass("icon_rot");
  }),
    $(".title-2").click(function () {
      $(".block-2").slideToggle(700), $(".icon-2").toggleClass("icon_rot");
    }),
    $(".title-3").click(function () {
      $(".block-3").slideToggle(700), $(".icon-3").toggleClass("icon_rot");
    }),
    $(".open_call").click(function () {
      $(".call, .background").fadeIn(300), $("body").addClass("fixed");
    }),
    $(".exit, .background").click(function () {
      $(".call, .background").fadeOut(300), $("body").removeClass("fixed");
    }),
    $(".call__back").click(function () {
      $(".good__resp").fadeOut(300),
        $(".form").fadeIn(300).css("display", "flex");
    }),
    $(".phone, .short-phone").each(function () {
      $(this).mask("+7 (999) 999-99-99");
    });
  let e = "",
    a = "",
    t = "",
    n = "",
    s = "",
    o = "",
    i = "",
    l = "",
    d = "",
    c = !0;
  $(".short-name").keyup(function () {
    (e = $(".short-name").val()),
      (c = !0),
      $(".short-name").removeClass("error");
  }),
    $(".name").keyup(function () {
      (t = $(".name").val()), (c = !0), $(".name").removeClass("error");
    }),
    $(".short-phone").keyup(function () {
      (a = $(".short-phone").val()),
        (c = !0),
        $(".short-phone").removeClass("error");
    }),
    $(".phone").keyup(function () {
      (n = $(".phone").val()), (c = !0), $(".phone").removeClass("error");
    }),
    $(".short-email").keyup(function () {
      l = $(".short-email").val();
    }),
    $(".email").keyup(function () {
      d = $(".email").val();
    }),
    $(".message").keyup(function () {
      (s = $(".message").val()), (c = !0), $(".message").removeClass("error");
    }),
    $(".city").keyup(function () {
      (o = $(".city").val()), (c = !0), $(".city").removeClass("error");
    }),
    $(".regist").keyup(function () {
      (i = $(".regist").val()), (c = !0), $(".regist").removeClass("error");
    }),
    $(".submit").click(async function () {
      if (
        ("" === e && ((c = !1), $(".short-name").addClass("error")),
        "" === a && ((c = !1), $(".short-phone").addClass("error")),
        "" === s && ((c = !1), $(".message").addClass("error")),
        c)
      ) {
        let t = new FormData();
        t.append("name", e),
          t.append("phone", a),
          t.append("email", l),
          t.append("message", s);
        let n = { method: "POST", body: t };
        (await fetch("https://fl-bankrotstvo.ru/onepage/short/", n)).ok &&
          ($(".form").fadeOut(300),
          $(".good__resp").fadeIn(300).css("display", "flex"));
      }
    });

  u = 0;

  $(".questions__btn-next , .head__btn").click(function () {
    $(".item-" + u).fadeOut(0),
      u++,
      $(".item-" + u)
        .fadeIn(500)
        .css("display", "flex");
  }),
    $(".questions__btn-back").click(function () {
      $(".item-" + u).fadeOut(0),
        u--,
        $(".item-" + u)
          .fadeIn(500)
          .css("display", "flex");
    });

  let f = "",
    p = "",
    m = "",
    v = "",
    h = [];
  $(".questions__btn-submit").click(async function () {
    if (
      ((f = $("input[name='question-1']:checked").val()),
      (p = $("input[name='question-2']:checked").val()),
      (m = $("input[name='question-3']:checked").val()),
      (v = $("input[name='question-4']:checked").val()),
      $.each($("input[name='question-5']:checked"), function () {
        h.push($(this).val());
      }),
      "" === t && ((c = !1), $(".name").addClass("error")),
      "" === n && ((c = !1), $(".phone").addClass("error")),
      "" === o && ((c = !1), $(".city").addClass("error")),
      "" === i && ((c = !1), $(".regist").addClass("error")),
      (void 0 !== f &&
        void 0 !== p &&
        void 0 !== m &&
        void 0 !== v &&
        void 0 !== h) ||
        ((c = !1), alert("Пожалуйста ответьте на все вопросы")),
      c)
    ) {
      console.log(f);
      let e = new FormData();
      e.append("summ", f),
        e.append("amount", p),
        e.append("income", m),
        e.append("pledge", v),
        e.append("property", h),
        e.append("city", o),
        e.append("registration_city", i),
        e.append("phone_number", n),
        e.append("email", d),
        e.append("name", t);
      let a = { method: "POST", body: e };
      (await fetch("https://fl-bankrotstvo.ru/onepage/full/", a)).ok &&
        ($(".item-" + u).fadeOut(1),
        u++,
        $(".item-" + u)
          .fadeIn(500)
          .css("display", "flex"));
    }
    $(".call__back__qustion").click(function () {
      $(".item-" + u).fadeOut(1), (u = 0), $(".item-" + u).fadeIn(500);
    });
  }),
    $('a[href*="#"]').on("click", function (e) {
      e.preventDefault(),
        $("html, body").animate(
          { scrollTop: $($(this).attr("href")).offset().top },
          500,
          "linear"
        );
    }),
    $(".advantages__item-1").hover(function () {
      $(".advantages-3, .advantages-2").fadeOut(0),
        $(".advantages-1").fadeIn(500).css("display", "flex"),
        $(this).addClass("focus"),
        $(".advantages__item-3 , .advantages__item-2").removeClass("focus");
    }),
    $(".advantages__item-2").hover(function () {
      $(".advantages-1, .advantages-3").fadeOut(0),
        $(".advantages-2").fadeIn(500).css("display", "flex"),
        $(this).addClass("focus"),
        $(".advantages__item-1 , .advantages__item-3").removeClass("focus");
    }),
    $(".advantages__item-3").hover(function () {
      $(".advantages-1, .advantages-2").fadeOut(0),
        $(".advantages-3").fadeIn(500).css("display", "flex"),
        $(this).addClass("focus"),
        $(".advantages__item-1 , .advantages__item-2").removeClass("focus");
    });
  let g = 1;
  $(".right_review").click(function () {
    $(".slide-" + g).fadeOut(0),
      4 === g ? (g = 1) : g++,
      $(".slide-" + g).fadeIn(300);
  }),
    $(".left_review").click(function () {
      $(".slide-" + g).fadeOut(0),
        1 === g ? (g = 4) : g--,
        $(".slide-" + g).fadeIn(300);
    }),
    $(window).scroll(function () {
      $(window).scrollTop() > 300 && $(".up").fadeIn(300),
        $(window).scrollTop() < 300 && $(".up").fadeOut(300);
    });
});
