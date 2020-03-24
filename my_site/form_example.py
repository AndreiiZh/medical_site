

# <div class="col-md-6">
#     <h2 class="text-center">Записаться на прием</h2>
#     <form method="post"> {% csrf_token %}
#         <div class="form-row">
#             <div class="form-group col-md-12">
#                 <p>Введите ваше имя</p>
#                 {% bootstrap_field form.fist_name show_label=False placeholder='Введите свое имя' %}
#                 <input type="text" class="form-control" placeholder="Введите свое имя">
#             </div>
#             <div class="form-group col-md-12">
#                 <p>Введите вашу фамилию</p>
#                 {{ form.last_name }}
#                 <input type="text" class="form-control" placeholder="Введите свою фамилию">
#             </div>
#             <div class="form-group col-md-12">
#                 <p>Введите ваш телефон</p>
#                 <input type="text" class="form-control" placeholder="+380xx-xxx-xx-xx">
#                 {{ form.phone_number }}
#             </div>
#             <div class="col text-right">
#                 <button type="submit" class="btn btn-primary" data-toggle="modal"
#                         data-dismiss="modal" data-target="#ok">Записаться
#                 </button>
#             </div>
#         </div>
#     </form>
# </div>


