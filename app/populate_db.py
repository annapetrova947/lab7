# app/populate_db.py

from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine

# Создаём все таблицы перед заполнением
models.Base.metadata.create_all(bind=engine)

# Определяем термины для заполнения
terms = [
    {
        "keyword": "Архитектурный паттерн (Architectural Pattern)",
        "description": "Повторяемая и обобщённая схема проектирования системы, определяющая структурные и поведенческие аспекты системы."
    },
    {
        "keyword": "Стейт-менеджер (State Manager)",
        "description": "Компонент, который управляет состоянием приложения, обеспечивая централизованный подход к хранению, изменению и распространению состояния между компонентами интерфейса."
    },
    {
        "keyword": "Состояние (State)",
        "description": "Направление и статус данных в приложении в определённый момент времени. Состояние может варьироваться от пользовательского ввода до полученных данных из API."
    },
    {
        "keyword": "Состояние приложения (Application State)",
        "description": "Общая информация, которая описывает текущее состояние всего приложения и может включать данные от различных компонентов."
    },
    {
        "keyword": "Контекст (Context)",
        "description": "Класс или объект, содержащий состояние приложения и передающий его во все дочерние компоненты, обычно используется в библиотеках, таких как React."
    },
    {
        "keyword": "Управление состоянием (State Management)",
        "description": "Процесс определения того, как и где хранить состояние приложения, а также как это состояние передается между компонентами и сервисами."
    },
    {
        "keyword": "MVC (Model-View-Controller)",
        "description": "Архитектурный паттерн, разделяющий приложение на три составные части: Модель (данные), Представление (интерфейс) и Контроллер (логика обработки)."
    },
    {
        "keyword": "MVVM (Model-View-ViewModel)",
        "description": "Архитектурный паттерн, в котором Представление связывается с ViewModel, а ViewModel управляет моделью и связывает её с Представлением через данные."
    },
    {
        "keyword": "MVP (Model-View-Presenter)",
        "description": "Архитектурный паттерн, в котором Presenter управляет логикой приложения и взаимодействует с Моделью и Представлением, предоставляя отделение логики от интерфейса."
    },
    {
        "keyword": "Flux",
        "description": "Архитектурный паттерн для управления состоянием в приложениях, который основан на однонаправленном потоке данных и включает действия, диспетчеры и стора."
    },
    {
        "keyword": "Redux",
        "description": "Библиотека для управления состоянием, основанная на паттерне Flux, которая позволяет хранить состояние приложения в одном 'сторе' и управлять им с помощью действий и редьюсеров."
    },
    {
        "keyword": "MobX",
        "description": "Библиотека для управления состоянием, которая обеспечивает реактивный подход, позволяющий автоматически отслеживать изменения состояния и обновлять интерфейс."
    },
    {
        "keyword": "Recoil",
        "description": "Библиотека управления состоянием для React, обеспечивающая низкоуровневый контроль над состоянием и его производительностью, обрабатывая как локальное, так и глобальное состояние."
    },
    {
        "keyword": "Context API",
        "description": "Встроенный API в React, позволяющий передавать данные через компоненты без необходимости передавать их явно через props, обеспечивая управление состоянием на уровне приложения."
    },
    {
        "keyword": "Синхронное управление состоянием (Synchronous State Management)",
        "description": "Подход к управлению состоянием, при котором изменения состояния применяются немедленно и не требуют дополнительных действий."
    },
    {
        "keyword": "Асинхронное управление состоянием (Asynchronous State Management)",
        "description": "Подход к управлению состоянием, который включает обработку асинхронных операций, таких как запросы к API, и управление состоянием на основе результатов этих операций."
    },
    {
        "keyword": "Декларативное управление состоянием (Declarative State Management)",
        "description": "Подход к управлению состоянием, при котором вы описываете, как должно выглядеть состояние приложения на основе его текущего состояния, а не непосредственно изменяете его."
    },
    {
        "keyword": "Эффекты (Effects)",
        "description": "Паттерн, который обрабатывает побочные эффекты в приложениях, включая асинхронные операции, такие как загрузка данных или подписки, обеспечивая разделение логики интерфейса и взаимодействия с внешними сервисами."
    },
    {
        "keyword": "Область видимости состояния (Scope of State)",
        "description": "Уровень, на котором состояние доступно в приложении, который может быть локальным (в пределах компонента) или глобальным (доступным для всего приложения)."
    },
    {
        "keyword": "Согласованность состояния (State Consistency)",
        "description": "Обеспечение того, чтобы состояние приложения оставалось корректным, актуальным и согласованным между различными компонентами и сервисами."
    },
    {
        "keyword": "Vuex",
        "description": "Стейт-менеджер для Vue.js, который управляет состоянием приложения и позволяет использовать хранилище с реактивностью Vue. Vuex использует концепции, такие как состояния, мутации и действия для управления изменениями состояния."
    },
    {
        "keyword": "Observable",
        "description": "Паттерн, который позволяет объектам оповещать другие объекты о изменениях своего состояния. В контексте MobX это реализуется через создание наблюдаемых данных (observable) и автоматическое реагирование на изменения через декораторы и функции."
    },
    {
        "keyword": "Effector",
        "description": "Система управления состоянием, основанная на концепциях реактивного программирования и потоков событий. Effector обеспечивает высокую производительность и предсказуемость состояния через использование событий и эффектов (effects)."
    },
    {
        "keyword": "Паттерн Event-Driven Architecture (EDA)",
        "description": "Архитектурный стиль, в котором действия инициируются событиями. В EDA система компонентов взаимодействует через обмен событиями, что обеспечивает гибкость и асинхронность. Effector позволяет легко обрабатывать события и эффекты, что делает его подходящим для EDA."
    },
    {
        "keyword": "Zustand",
        "description": "Простая и производительная библиотека управления состоянием для React, предлагающая два ключевых принципа: отсутствие обременительных шаблонов и возможность управления состоянием через хуки (hooks). Zustand позволяет создавать хранилища с минимальным количеством кода."
    }
]





def populate():
    db: Session = SessionLocal()
    try:
        existing_terms = db.query(models.Term).count()
        if existing_terms == 0:
            for term_data in terms:
                term = models.Term(**term_data)
                db.add(term)
            db.commit()
            print("База данных успешно заполнена начальными терминами.")
        else:
            print("База данных уже содержит данные. Пропуск заполнения.")
    except Exception as e:
        db.rollback()
        print(f"Ошибка при заполнении базы данных: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    populate()