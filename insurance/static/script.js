document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('insuranceForm');
    const insurancePlan = document.getElementById('insurancePlan'); // مطمئن شوید که این ID درست است
    const paymentMethod = document.getElementById('paymentMethod'); // مطمئن شوید که این ID درست است
    const totalPriceInput = document.getElementById('totalPrice');

    // تابع برای محاسبه مبلغ کل
    function calculateTotalPrice() {
        let basePrice = 1000000; // قیمت پایه پیش‌فرض (می‌توانید این مقدار را بسته به طرح تغییر دهید)

        // تغییر قیمت پایه بسته به طرح انتخاب شده
        if (insurancePlan.value === "one year") {
            basePrice = 1000000; // قیمت پایه برای طرح یک ساله
        } else if (insurancePlan.value === "four years") {
            basePrice = 3000000; // قیمت پایه برای طرح چهار ساله
        } else if (insurancePlan.value === "eight years") {
            basePrice = 8000000; // قیمت پایه برای طرح هشت ساله
        }

        // تغییر فاکتور پرداخت بسته به روش پرداخت انتخابی
        let paymentFactor = 1; // فاکتور پیش‌فرض برای پرداخت یکجا

        if (paymentMethod.value === "yearly") {
            paymentFactor = 1.5; // پرداخت سالیانه
        } else if (paymentMethod.value === "monthly") {
            paymentFactor = 1.15; // پرداخت ماهیانه (ضرب در 12)
        } else if (paymentMethod.value === "complete") {
            paymentFactor = 1; // پرداخت کامل به صورت یکجا
        }

        // محاسبه مبلغ کل با توجه به انتخاب‌های طرح و روش پرداخت
        let totalPrice = basePrice * paymentFactor;
        totalPriceInput.value = totalPrice.toLocaleString() + ' تومان'; // نمایش مبلغ به فرمت ریال
    }

    // اضافه کردن شنونده رویداد برای تغییر انتخاب طرح یا روش پرداخت
    insurancePlan.addEventListener('change', calculateTotalPrice);
    paymentMethod.addEventListener('change', calculateTotalPrice);

    // محاسبه اولیه مبلغ کل هنگام بارگذاری صفحه
    calculateTotalPrice();

    // هندل کردن ارسال فرم
    form.addEventListener('submit', function(e) {
        alert('فرم با مبلغ کل ارسال شد: ' + totalPriceInput.value);
    });
    calculateTotalPrice();
});
