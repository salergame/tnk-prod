// Данные для услуг
const serviceItems = [
    {
        title: "Оценка недвижимости",
        description: "Качественная оценка недвижимости в кратчайшие сроки",
        image: "static/deps/images/services/real-estate.jpg",
        process: "Процесс оценки недвижимости включает:\n• Осмотр объекта\n• Сбор данных о характеристиках\n• Анализ рыночных цен\n• Определение ценообразующих факторов\n• Применение трех методов оценки (сравнительный, доходный, затратный)"
      },
      {
        title: "Оценка движимого имущества",
        description: "Четкая и не затратная оценка транспортных средств",
        image: "static/deps/images/services/movable-property.jpg",
        process: "Методология оценки движимого имущества:\n• Визуальный осмотр\n• Документирование технических характеристик\n• Определение износа\n• Учет рыночных цен\n• Анализ технического состояния\n• Применение сравнительного метода"
      },
      {
        title: "Оценка бизнеса",
        description: "Справедливая оценка стоимости бизнеса и имущества",
        image: "static/deps/images/services/business.jpg",
        process: "Этапы оценки бизнеса:\n• Анализ финансовой отчетности\n• Изучение структуры активов\n• Оценка интеллектуальной собственности\n• Применение доходного подхода\n• Учет рыночной конъюнктуры\n• Анализ рисков бизнеса"
      },
      {
        title: "Оценка интеллектуальной собственности",
        description: "Быстрая оценка стоимости интеллектуальной собственности",
        image: "static/deps/images/services/intellectual-property.jpg",
        process: "Оценка интеллектуальной собственности включает:\n• Идентификация объекта\n• Определение правового статуса\n• Расчет роялти\n• Анализ аналогичных сделок\n• Учет затрат на создание\n• Оценка коммерческого потенциала"
      },
      {
        title: "Оценка прав недропользования",
        description: "Профессиональная оценка прав на добычу полезных ископаемых",
        image: "static/deps/images/services/mining-rights.jpg",
        process: "Методика оценки прав недропользования:\n• Геологическое изучение участка\n• Анализ запасов ископаемых\n• Изучение лицензионных условий\n• Расчет потенциального дохода\n• Учет рисков разработки\n• Анализ налоговых обязательств"
      },
      {
        title: "Оценка биологических активов",
        description: "Оценка стоимости биологических ресурсов и активов",
        image: "static/deps/images/services/biological-assets.jpg",
        process: "Процесс оценки биологических активов:\n• Инвентаризация\n• Определение возраста и состояния\n• Учет затрат на выращивание\n• Расчет рыночной стоимости\n• Оценка продуктивности\n• Учет биологических циклов"
      },
      {
        title: "Оценка воздушных и морских судов",
        description: "Специализированная оценка водного и воздушного транспорта",
        image: "static/deps/images/services/ships-aircraft.jpg",
        process: "Этапы оценки судов:\n• Инспекция технического состояния\n• Проверка документации\n• Анализ истории эксплуатации\n• Учет наработки и модификаций\n• Анализ рыночных данных\n• Расчет остаточного ресурса"
      },
      {
        title: "Оценка железнодорожного транспорта",
        description: "Экспертная оценка железнодорожного подвижного состава",
        image: "static/deps/images/services/railway.jpg",
        process: "Методология оценки ж/д транспорта:\n• Осмотр подвижного состава\n• Анализ технических характеристик\n• Проверка документации\n• Учет истории ремонтов\n• Применение затратного метода\n• Расчет остаточного срока эксплуатации"
      },
      {
        title: "Оценка легкового автомобиля",
        description: "Оценка рыночной стоимости легковых автомобилей",
        image: "static/deps/images/services/car.jpg",
        process: "Этапы оценки автомобиля:\n• Осмотр транспортного средства\n• Проверка документации\n• Учет марки, модели, года выпуска\n• Анализ технического состояния\n• Изучение истории ДТП\n• Сравнение с рыночными ценами"
      },
      {
        title: "Оценка незавершенного строительства",
        description: "Точная оценка объектов незавершенного строительства",
        image: "static/deps/images/services/construction.jpg",
        process: "Процедура оценки незавершенного строительства:\n• Обследование объекта\n• Определение степени готовности\n• Анализ проектной документации\n• Расчет затрат на завершение\n• Учет износа конструкций\n• Оценка потенциала объекта"
      },
      {
        title: "Оценка земельного участка",
        description: "Профессиональная оценка земельных участков различного назначения",
        image: "static/deps/images/services/land.jpg",
        process: "Методика оценки земельного участка:\n• Анализ документов\n• Осмотр местности\n• Определение характеристик участка\n• Учет местоположения и инфраструктуры\n• Применение метода сравнения продаж\n• Анализ градостроительных ограничений"
      },
      {
        title: "Оценка спецтехники",
        description: "Экспертная оценка специализированной техники и оборудования",
        image: "static/deps/images/services/machinery.jpg",
        process: "Этапы оценки специальной техники:\n• Осмотр и проверка состояния\n• Изучение документации\n• Учет наработки моточасов\n• Анализ технического состояния узлов\n• Сравнение с аналогичной техникой\n• Расчет остаточного ресурса"
      },
      {
        title: "Оценка акций",
        description: "Профессиональная оценка акций и ценных бумаг",
        image: "static/deps/images/services/business.jpg",
        process: "Процедура оценки акций:\n• Анализ финансовой отчетности\n• Изучение рыночных котировок\n• Оценка перспектив компании\n• Применение доходного подхода\n• Расчет мультипликаторов\n• Учет факторов ликвидности"
      },
      {
        title: "Оценка стартапов",
        description: "Независимая оценка инновационных проектов и стартапов",
        image: "static/deps/images/services/business.jpg",
        process: "Методология оценки стартапов:\n• Анализ бизнес-модели\n• Оценка потенциала рынка\n• Изучение команды проекта\n• Применение венчурного метода\n• Учет рисков и неопределенности\n• Оценка потенциала масштабирования"
      },
      {
        title: "Оценка оборудования",
        description: "Точная оценка промышленного и специализированного оборудования",
        image: "static/deps/images/services/machinery.jpg",
        process: "Этапы оценки оборудования:\n• Осмотр и определение состояния\n• Изучение технических характеристик\n• Учет года выпуска и мощности\n• Расчет стоимости замещения\n• Анализ рынка аналогов\n• Учет затрат на монтаж"
      },
      {
        title: "Оценка жилого дома",
        description: "Всесторонняя оценка частных домов и коттеджей",
        image: "static/deps/images/services/real-estate.jpg",
        process: "Процедура оценки жилого дома:\n• Осмотр здания\n• Изучение документации\n• Учет площади и планировки\n• Оценка материалов и коммуникаций\n• Сравнительный анализ\n• Расчет стоимости строительства"
      },
      {
        title: "Оценка квартиры",
        description: "Профессиональная оценка квартир любого типа и площади",
        image: "static/deps/images/services/real-estate.jpg",
        process: "Методика оценки квартиры:\n• Осмотр помещения\n• Изучение документации\n• Учет планировки и этажа\n• Оценка состояния и коммуникаций\n• Анализ инфраструктуры района\n• Сравнение с аналогичными объектами"
      }
];

// Данные для сертификатов
const certificates = [
  {
    title: "Сертификат",
    image: "static/deps/images/certificates/Жаксалыков Кайрат Куанышпаевич.png"
  },
  {
    title: "Сертификат",
    image: "static/deps/images/certificates/Жаксалыков Кайрат Куанышпаевич1.png"
  },
  {
    title: "Сертификат",
    image: "static/deps/images/certificates/Жаксалыков Кайрат Куанышпаевич2.png"
  },
  {
    title: "Сертификат",
    image: "static/deps/images/certificates/Недвижимое имущество.png"
  },
  {
    title: "Сертификат",
    image: "static/deps/images/certificates/Недвижимое.png"
  },
  {
    title: "Сертификат",
    image: "static/deps/images/certificates/Движимое имущество.png"
  },
  {
    title: "Сертификат",
    image: "static/deps/images/certificates/Движимое.png"
  },
  {
    title: "Сертификат",
    image: "static/deps/images/certificates/Свидетельство палаты 2024 г..png"
  },
  {
    title: "Сертификат",
    image: "static/deps/images/certificates/Интелектуальной собственности.png"
  },
  {
    title: "Сертификат",
    image: "static/deps/images/certificates/Интелектуалка.png"
  },
  {
    title: "Сертификат",
    image: "static/deps/images/certificates/Әділханова Назерке.png"
  },
  {
    title: "Сертификат",
    image: "static/deps/images/certificates/Әділханова Назерке1.png"
  },
  {
    title: "Сертификат",
    image: "static/deps/images/certificates/Әділханова Назерке2.png"
  },
  {
    title: "Сертификат",
    image: "static/deps/images/certificates/Әділханова Назерке3.png"
  },
  {
    title: "Сертификат",
    image: "static/deps/images/certificates/Әділханова Назерке4.png"
  },
  {
    title: "Сертификат",
    image: "static/deps/images/certificates/Әділханова Назерке5.png"
  },
  {
    title: "Сертификат",
    image: "static/deps/images/certificates/Әділханова Назерке Әмірханқызы 28.09.2023.png"
  },
  {
    title: "Сертификат",
    image: "static/deps/images/certificates/Әділханова Назерке Әмірханқызы 12.10.2023.png"
  },
  {
    title: "Сертификат",
    image: "static/deps/images/certificates/Әділханова Назерке Әмірханқызы 2024 г..png"
  },
  {
    title: "Сертификат",
    image: "static/deps/images/certificates/1.png"
  }
];

// DOM элементы
document.addEventListener('DOMContentLoaded', function() {
  // Мобильное меню
  const menuBtn = document.querySelector('.mobile-menu-btn');
  const mobileMenu = document.querySelector('.mobile-menu');
  const menuIcon = menuBtn.querySelector('[data-lucide="menu"]');
  
  if (menuBtn) {
    menuBtn.addEventListener('click', function() {
      mobileMenu.classList.toggle('active');
      
      // Изменение иконки при открытии/закрытии меню
      if (mobileMenu.classList.contains('active')) {
        menuIcon.closest('i').setAttribute('data-lucide', 'x');
      } else {
        menuIcon.closest('i').setAttribute('data-lucide', 'menu');
      }
      
      // Обновление иконок
      lucide.createIcons();
    });
  }
  
  // Обработка карточек услуг
  const serviceCards = document.querySelectorAll('.service-card');
  const serviceModal = document.getElementById('service-modal');
  const serviceTitle = document.getElementById('service-title');
  const serviceDescription = document.getElementById('service-description');
  const serviceImage = document.getElementById('service-image');
  const serviceProcess = document.getElementById('service-process');
  const closeModalBtns = document.querySelectorAll('.modal-close');
  
  // Открытие модального окна услуги
  serviceCards.forEach(card => {
    card.addEventListener('click', function() {
      const serviceIndex = this.getAttribute('data-service');
      const service = serviceItems[serviceIndex];
      const cardImage = this.querySelector('.service-image img'); // Находим img внутри карточки
      
      serviceTitle.textContent = service.title;
      serviceDescription.textContent = service.description;
      // Используем src из img карточки
      if (cardImage) {
        serviceImage.src = cardImage.src;
      } else {
        serviceImage.src = ''; // Установить пустой src, если изображение не найдено
      }
      serviceImage.alt = service.title;
      serviceProcess.textContent = service.process;
      
      serviceModal.classList.add('active');
      document.body.style.overflow = 'hidden'; // Блокировка прокрутки страницы
    });
  });
  
  // Обработка карточек сертификатов
  const certificateCards = document.querySelectorAll('.certificate-card');
  const certificateModal = document.getElementById('certificate-modal');
  const certificateDocument = document.getElementById('certificate-document');
  
  // Открытие модального окна сертификата
  certificateCards.forEach(card => {
    card.addEventListener('click', function() {
      const cardImage = this.querySelector('.certificate-image img'); // Находим img внутри карточки
      
      // Используем src из img карточки
      if (cardImage) {
        certificateDocument.src = cardImage.src; 
      } else {
        certificateDocument.src = ''; // Установить пустой src, если изображение не найдено
      }
      certificateDocument.alt = "Сертификат"; // Используем обобщенное название для alt
      
      certificateModal.classList.add('active');
      document.body.style.overflow = 'hidden';
    });
  });
  
  // Закрытие модальных окон
  closeModalBtns.forEach(btn => {
    btn.addEventListener('click', function() {
      this.closest('.modal').classList.remove('active');
      document.body.style.overflow = '';
    });
  });
  
  // Закрытие модального окна по клику вне контента
  const modals = document.querySelectorAll('.modal');
  modals.forEach(modal => {
    modal.addEventListener('click', function(e) {
      if (e.target === this) {
        this.classList.remove('active');
        document.body.style.overflow = '';
      }
    });
  });
  
  // Карусель
  const carouselTrack = document.querySelector('.carousel-track');
  const carouselItems = document.querySelectorAll('.carousel-track .service-card');
  const prevBtn = document.querySelector('.carousel-btn.prev');
  const nextBtn = document.querySelector('.carousel-btn.next');
  let currentIndex = 0;
  let itemWidth = 0;
  let itemsPerView = 1; // По умолчанию для мобильных
  
  // Карусель сертификатов
  const certificatesTrack = document.querySelector('.certificates-track');
  const certificateItems = document.querySelectorAll('.certificates-track .certificate-card');
  const certPrevBtn = document.querySelector('.carousel-btn.cert-prev');
  const certNextBtn = document.querySelector('.carousel-btn.cert-next');
  let certCurrentIndex = 0;
  let certItemWidth = 0;
  let certItemsPerView = 1;
  let autoScrollInterval = null;
  
  function updateCarouselDimensions() {
    if (!carouselTrack || carouselItems.length === 0) return;
    
    // Определяем размер элемента и количество видимых элементов в зависимости от ширины экрана
    const containerWidth = document.querySelector('.carousel-container').offsetWidth;
    
    if (window.innerWidth >= 1024) {
      itemsPerView = 3;
    } else if (window.innerWidth >= 768) {
      itemsPerView = 2;
    } else {
      itemsPerView = 1;
    }
    
    // Вычисляем ширину элемента с учетом отступов (gap)
    const gap = 2; // размер отступа в rem
    const gapInPx = gap * 16; // примерное преобразование rem в px
    const totalGapWidth = gapInPx * (itemsPerView - 1);
    const availableWidth = containerWidth - totalGapWidth;
    itemWidth = availableWidth / itemsPerView;
    
    // Устанавливаем ширину элементов
    carouselItems.forEach(item => {
      item.style.flex = `0 0 ${itemWidth}px`;
      item.style.minWidth = `${itemWidth}px`;
      item.style.maxWidth = `${itemWidth}px`;
    });
    
    // Сбрасываем позицию карусели при изменении размеров
    currentIndex = 0;
    
    // Обновляем позицию карусели
    updateCarouselPosition();
  }
  
  function updateCertificatesCarouselDimensions() {
    if (!certificatesTrack || certificateItems.length === 0) return;
    
    // Определяем размер элемента и количество видимых элементов в зависимости от ширины экрана
    const containerWidth = document.querySelector('.certificates-carousel .carousel-container').offsetWidth;
    
    if (window.innerWidth >= 1024) {
      certItemsPerView = 5;
    } else if (window.innerWidth >= 768) {
      certItemsPerView = 3;
    } else if (window.innerWidth >= 640) {
      certItemsPerView = 2;
    } else {
      certItemsPerView = 1;
    }
    
    // Вычисляем ширину элемента с учетом отступов (gap)
    const gap = 2; // размер отступа в rem
    const gapInPx = gap * 16; // примерное преобразование rem в px
    const totalGapWidth = gapInPx * (certItemsPerView - 1);
    const availableWidth = containerWidth - totalGapWidth;
    certItemWidth = availableWidth / certItemsPerView;
    
    // Устанавливаем ширину элементов
    certificateItems.forEach(item => {
      item.style.flex = `0 0 ${certItemWidth}px`;
      item.style.minWidth = `${certItemWidth}px`;
      item.style.maxWidth = `${certItemWidth}px`;
    });
    
    // Сбрасываем позицию карусели при изменении размеров
    certCurrentIndex = 0;
    
    // Обновляем позицию карусели
    updateCertificatesCarouselPosition();
    
    // Запускаем автоматическую прокрутку
    startAutoScroll();
  }
  
  function updateCertificatesCarouselPosition() {
    if (!certificatesTrack) return;
    
    const gap = 2 * 16; // gap в px
    const offsetX = certCurrentIndex * (certItemWidth + gap);
    certificatesTrack.style.transform = `translateX(-${offsetX}px)`;
    
    // Обновляем состояние кнопок
    if (certPrevBtn) certPrevBtn.disabled = certCurrentIndex <= 0;
    if (certNextBtn) certNextBtn.disabled = certCurrentIndex >= certificateItems.length - certItemsPerView - 3; // -3 для дублированных элементов
  }
  
  function startAutoScroll() {
    // Останавливаем предыдущий интервал если он был запущен
    if (autoScrollInterval) {
      clearInterval(autoScrollInterval);
    }
    
    // Запускаем автоматическую прокрутку каждые 2 секунды
    autoScrollInterval = setInterval(() => {
      if (certCurrentIndex < certificateItems.length - certItemsPerView - 3) {
        certCurrentIndex++;
      } else {
        // Перематываем в начало для бесконечной прокрутки
        certCurrentIndex = 0;
      }
      updateCertificatesCarouselPosition();
    }, 2000);
  }
  
  function updateCarouselPosition() {
    if (!carouselTrack) return;
    
    const gap = 2 * 16; // gap в px
    const offsetX = currentIndex * (itemWidth + gap);
    carouselTrack.style.transform = `translateX(-${offsetX}px)`;
    
    // Обновляем состояние кнопок
    if (prevBtn) prevBtn.disabled = currentIndex <= 0;
    if (nextBtn) nextBtn.disabled = currentIndex >= carouselItems.length - itemsPerView;
  }
  
  // Обработка кнопок для карусели сертификатов
  if (certPrevBtn && certNextBtn && certificatesTrack) {
    certPrevBtn.addEventListener('click', function() {
      if (certCurrentIndex > 0) {
        certCurrentIndex--;
        updateCertificatesCarouselPosition();
        
        // Перезапускаем автопрокрутку после клика
        startAutoScroll();
      }
    });
    
    certNextBtn.addEventListener('click', function() {
      if (certCurrentIndex < certificateItems.length - certItemsPerView - 3) {
        certCurrentIndex++;
        updateCertificatesCarouselPosition();
        
        // Перезапускаем автопрокрутку после клика
        startAutoScroll();
      } else {
        // Переход в начало при достижении конца
        certCurrentIndex = 0;
        updateCertificatesCarouselPosition();
        startAutoScroll();
      }
    });
    
    // Останавливаем автопрокрутку при наведении на карусель
    certificatesTrack.addEventListener('mouseenter', function() {
      if (autoScrollInterval) {
        clearInterval(autoScrollInterval);
      }
    });
    
    // Возобновляем автопрокрутку при уходе мыши
    certificatesTrack.addEventListener('mouseleave', function() {
      startAutoScroll();
    });
    
    // Добавляем стили для состояния disabled
    certPrevBtn.disabled = true; // Изначально первая кнопка disabled
  }
  
  if (prevBtn && nextBtn && carouselTrack) {
    prevBtn.addEventListener('click', function() {
      if (currentIndex > 0) {
        currentIndex--;
        updateCarouselPosition();
      }
    });
    
    nextBtn.addEventListener('click', function() {
      if (currentIndex < carouselItems.length - itemsPerView) {
        currentIndex++;
        updateCarouselPosition();
      }
    });
    
    // Добавляем стили для состояния disabled
    prevBtn.disabled = true; // Изначально первая кнопка disabled
    
    // Стили для disabled кнопок
    const style = document.createElement('style');
    style.textContent = `
      .carousel-btn:disabled {
        opacity: 0.5;
        cursor: not-allowed;
      }
    `;
    document.head.appendChild(style);
  }
  
  // Инициализация карусели
  if (carouselTrack) {
    // Задержка для инициализации карусели после полной загрузки страницы
    setTimeout(updateCarouselDimensions, 100);
    
    // Обновление размеров при изменении размера окна
    window.addEventListener('resize', updateCarouselDimensions);
  }
  
  // Инициализация карусели сертификатов
  if (certificatesTrack) {
    // Задержка для инициализации карусели после полной загрузки страницы
    setTimeout(updateCertificatesCarouselDimensions, 100);
    
    // Обновление размеров при изменении размера окна
    window.addEventListener('resize', updateCertificatesCarouselDimensions);
  }
  
  // Плавная прокрутка к секциям по якорным ссылкам
  const anchorLinks = document.querySelectorAll('a[href^="#"]');
  anchorLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      
      const targetId = this.getAttribute('href').substring(1);
      const targetElement = document.getElementById(targetId);
      
      if (targetElement) {
        // Закрываем мобильное меню, если оно открыто
        if (mobileMenu.classList.contains('active')) {
          mobileMenu.classList.remove('active');
          menuIcon.closest('i').setAttribute('data-lucide', 'menu');
          lucide.createIcons();
        }
        
        window.scrollTo({
          top: targetElement.offsetTop - 70, // Учитываем высоту шапки
          behavior: 'smooth'
        });
      }
    });
  });
}); 