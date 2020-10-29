import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Output, Input, State
import dash_bootstrap_components as dbc


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
                dbc.NavbarSimple(
                    brand="Pycoders.nl/SQL Module",
                    brand_href="/home",
                    color="danger",
                    dark=True,
                ),
                dbc.Row([
                    dbc.Col([
                        dbc.ListGroup([
                            dbc.ListGroupItem("Giris", id='giris', n_clicks=0, color='secondary'),
                            dbc.ListGroupItem("Proje", id='proje', n_clicks=0, color='secondary'),
                            dbc.ListGroupItem("Sema", id='sema', n_clicks=0, color='secondary'),
                            dbc.ListGroupItem("Tablolar", id='tablo', n_clicks=0, color='secondary'),
                            dbc.ListGroupItem("CRUD", id='crud', n_clicks=0, color='secondary'),
                            dbc.ListGroupItem("Import", id='importt', n_clicks=0, color='secondary'),
                            dbc.ListGroupItem("Sorgular", id='sorgu', n_clicks=0, color='secondary'),
                            dbc.ListGroupItem("Export", id='exportt', n_clicks=0, color='secondary'),
                            dbc.ListGroupItem("Dashboard", id='dashboard', n_clicks=0, color='secondary'),
                            dbc.ListGroupItem("Sonuc", id='sonuc', n_clicks=0, color='secondary'),
                        ]),
                        html.P(''),
                        html.P('Bazi konulari hatirlamiyor musun?'),
                        html.P('Ya da tam anlasilmayan yerler mi var?'),
                        html.U([
                            html.Li(html.A('Semih abinin sayfasina link', href='')),
                            html.Li(html.A('PostgreSQL nin sayfasina link', href='')),
                            html.Li(html.A('Mongo DB nin sayfasina link', href='')),
                        ])
                    ], width=3),

                    dbc.Col(
                        html.Div(id='page-content-1'), width=5),

                    # dbc.Button("Goster", id="open-centered"),
                    # dbc.Modal([
                    #         dbc.ModalHeader("Header"),
                    #         html.Div(html.Img(src='/assets/relations schema.png', height='750', width='1000')),
                    #         dbc.ModalFooter(dbc.Button("Close", id="close-centered", color="danger", n_clicks=0, className="ml-auto"))
                    #     ], id="modal-centered", centered=True),

                ], justify='start')
            ])

@app.callback (
              Output('page-content-1', 'children'),
              [Input('giris', 'n_clicks'),
               Input('proje', 'n_clicks'),
               Input('sema', 'n_clicks'),
               Input('tablo', 'n_clicks'),
               Input('crud', 'n_clicks'),
               Input('importt', 'n_clicks'),
               Input('sorgu', 'n_clicks'),
               Input('exportt', 'n_clicks'),
               Input('dashboard', 'n_clicks'),
               Input('sonuc', 'n_clicks')]
              )
def display_page(n_clicks_1, n_clicks_2,  n_clicks_3, n_clicks_4, n_clicks_5, n_clicks_6, n_clicks_7, n_clicks_8, n_clicks_9, n_clicks_10):

    # style1 = {'display': 'none'}
    # style2 = {'display': 'flex'}

    ctx = dash.callback_context
    pie = ctx.triggered[0]['prop_id'].split('.')[0]

    if pie == 'giris':
        return html.Div([
                    html.H1('SQL projesine hosgeldiniz...'),
                    html.H3('Neler ogrendik?'),
                    html.U([
                        html.Li('DB nedir? DB cesitleri nelerdir?'),
                        html.Li('DB nasil olusturulur?'),
                        html.Li('Table relations semasi nasil kurulur?'),
                        html.Li('SQL-NoSQL?'),
                        html.Li('Query komutlari nelerdir?'),
                        html.Li('PosrgreSQL'),
                        html.Li('Mongo DB'),
                    ]),
                    html.P(''),
                    html.P('Bu proje ile gectigimiz 3 hafta boyunca gordugumuz konulari pekistirecegiz.'),
                    html.P('Projemizi 2. hafta gordugumuz PostgreSQL kullanarak gerceklestirecegiz.'),
                    html.P("Projede kulanacagimiz veri ise 'Northwind sample database' verisi olacak."),
                    html.P('Ayrica arayuz tasariminda ise Plotly.Dash kutuphanesini kullanacagiz.'),
                    html.P(
                        'Projedeki asil gayemiz, bir database tum yollardan ulasmaya calismak ve istedigimiz islemleri uygulamak'),
                    html.P('Bunun icin projemizi yaparken 3 yol kullanacagiz.'),
                    html.P(
                        'Ilk olarak PostgreSQL in arayuzunu kullanarak tablo olusturacak ve sorgularimizi gerceklestirecegiz.'),
                    html.P('Sonrasinda Pycharm gibi bir IDE uzerinden ayni islemleri gerceklestirecegiz'),
                    html.P(
                        'Son olarak ise baska bir arayuz uzerinden buttonlara kendimiz fonksiyonellik kazandirarak ayni islemleri yapacagiz'),
                    html.P('Bu, ayni zamanda user olarak bir tusa bastigimizda arka planda neler oldugunu gormemizi saglayacak'),
                    html.P('Okuyunca havali geliyor degil mi?'),
                    html.P('Gercekte de havali :)'),
                    html.P('Eger bu projeyi istenilen sekilde yaparsaniz github hesabiniza yukleyebileceginiz ve CV nizde rahatlikla gosterebileceginiz guzel bir projeniz olmus olacak.'),
                    html.P('Sizi daha fazla heyecanlandirmadan hadi baslayalim'),

                ],className='mt-3')

    elif pie == 'proje':
        return html.Div([
                    html.H3('Bu projede neler yapacaksiniz? '),
                    html.U([
                        html.Li('Uretim yapan bir firmanin database ni olusturmak'),
                        html.Li('Table relations semasini olusturmak'),
                        html.Li('Tablolari oluşturmak'),
                        html.Li('CRUD komutlarini kullanmak'),
                        html.Li('Query komutlari ile istedigimiz veri tablosunu olusturmak'),
                        html.Li('Import/Export yapmak'),
                        html.Li('Bir arayuz uzerinden DB islemlerini gerceklestirmek')
                    ]),
                    html.P(''),
                    html.P('Evet daha once de soyledigimiz gibi amaclarimizdan bir tanesi guzel bir dashboard yapmak ve db ye bu dashboard uzerinden erismek'),
                    html.P('Bu dashboard u yaparken Plot.Dash kullanacagiz ama sizin bu kutuphaneyi bilmediginizi biliyoruz'),
                    html.P('O yuzden size biraz yardim edelim dedik ve arayuzu biz tasarladik'),
                    html.P('Hepsini degil tabi, onemli kisimlarini yani islevsellik kazandirilmasi gereken kisimlarini size biraktik'),
                    html.P('Amacimiz sizin python ile DB ye baglanmaniz, bunu bu arayuz ile gerceklestirebilirseniz, her arayuzle gerceklestirebilirsiniz, cunku python kodlarimiz hic degismeyecek'),
                    html.P('Simdi bizim tasarladigimiz arayuzu bilgisayariniza indirmenizi istiyoruz.'),
                    html.P('Bunun icin ... reposuna gidin ve ... forklayin'),
                    html.P('Bu islemleri kursun ilk haftalarinda git/github kisminda ogrenmistiniz ancak hatirlamiyorsaniz bu videodan bakabilirsiniz.'),
                    html.P('Bilgisayariniza indirdiginiz dosyayi acin ve index.py dosyasini run edin.'),
                    html.P('Hata aldiniz degil mi?'),
                    html.P('Muhtemelen error olarak size ilgili kutuphaneleri yuklemediginizi soyluyor'),
                    html.P('Dikkat ederseniz dosyanin basinda birsuru kutuphane import etmisiz ancak bu kutuplanelerin bir kismi sizde yuklu degil'),
                    html.P('Once bu projenin calismasi icin hangi kutuphanelerini yuklenmesi gerektigini ogrenelim.'),
                    html.P('Sol tarafta "requirement.txt" diye bir dosya var, dosyanin icinde gerekli kutuphaneler yaziyor.'),
                    html.P('Bu kutuphaneleri yuklememiz lazim ama teker teker degil, teker teker de yapabilirz ancak kissa yolu var.'),
                    html.P('Pycharm terminalini acin ve pip install -r requirements.txt yazin.'),
                    html.P('Bu komut requirements.txt dosyasindaki kutuphaneleri billgisayariniza yukleyecektir.'),
                    html.P('Yukleme islemi bittikten sonra index.py dosyasini tekrar run edin'),
                    html.P('Muhtemelen calismistir'),
                    # html.P('https://www.pinterest.fr/pin/346143921362026822/'),
                    # html.P('https://dribbble.com/shots/2934538-VirtualHealth'),
                    # html.P('https://dribbble.com/shots/3649672-dashboard?utm_source=Pinterest_Shot&utm_campaign=Designoholic&utm_content=dashboard&utm_medium=Social_Share'),
                    html.P('Artik sema bolumune gecebiliriz')

                ], className='mt-3')

    elif pie =='sema':
        return html.Div([
                    html.H3('Table Relations Semasinin olusturulmasi'),
                    html.P('Table relations semasi neydi? Hatirlamiyorsaniz sol alttaki linkten bakabilirsiniz.'),
                    html.P('Table relations semasi ya da diagrami bir DB olusturuken dusunulmasi gereken en onemli konudur.'),
                    html.P('Cunku DB karmasik bir yapidir, onlarca, yuzlerce tabloyu icerebilir ve bu tablolar birbirine baglidir.'),
                    html.P('Iyi dusunmeden olusturdugunuz bir DB de ileride bir degisiklik yapmak tum DB nizi etkileyebilir.'),
                    html.P('Peki sizden ne istiyoruz?'),
                    html.P('Uretim yapan bir firmanin database yapmak istiyoruz demistik. Sizce bu DB nin table relations semasi nasil olmali?'),
                    html.P('Bir uretim firmasinda hangi departmanlarin oldugunu ve bu departmanlarin hangi bilgileri tutmak isteyecegini dusunerek ise baslayabilirsiniz'),
                    html.P('Bunun uzerine en bir saat dusunup bir sema cikarmanizi istiyoruz. Cikardiginiz semayi ... reposuna yukleyin.'),
                    html.P('Size bu semayi cizdirmeden de projemize devam edebilirdik ve bu bizim projemizi hic etkilemezdi.'),
                    html.P('Ama bu cok buyuk bir eksiklik olurdu, cunku bir daha muhtemelen hicbir zaman bu semayi cizmeyeceksiniz.'),
                    html.P('Yani bu sizin icin iyi bir firsat'),
                    html.P('SQL ile ilgili mulakat sorularina bakarsaniz bazi firmalarin ise alirken benzer semalar sorduklarini gorebilirsiniz.'),
                    html.P('Umarim size de sorarlar cunku artik biliyorsunuz:)'),
                    html.P('Neyse sizi daha fazla yormayalim ve bu projede uzerinden ilerleyecegimiz semayi gosterelim.'),

                ], className='mt-3')


    elif pie == 'tablo':
        return html.Div([
                    html.H3('Tablolarin Olusturulmasi'),
                    html.P('Daha once de bahsettigimiz gibi projemiz yaparken 3 yol kullanacagiz.'),
                    html.U([
                        html.Li('PostgreSQL arayuzunu kullanarak'),
                        html.Li('Pycharm i kullanarak'),
                        html.Li('Daha once tasarladigimiz bir arayuzu kullanarak'),
                    ]),
                    html.P('Hazir misiniz?'),
                    html.P('Oncelikle PostgreSQL arayuzunu acin ve ... adinda bir DB olusturun'),
                    html.P('Sonra kullanacagimiz semaya bakarak 9 tablodan 3 tanesini ** SQL komutlari kullanmadan olusturun **'),
                    html.P('Simdi de kalan 6 tablodan 3 tanesini PostgreSQL arayuzunden ** SQL komutlarini kullanarak olusturun ** '),
                    html.P('DB nizi refresh edin 6 tablo goruyorsunuz degil mi?'),
                    html.P('Simdi Pycharm uzerinden baglanma zamani..'),
                    html.P('Daha once githubtan locale kopyaladiginiz ... klasorunu acin'),
                    html.P('...dosyasini acin ve en ust kisma Pythonin PostgreSQL e baglanmasi icin gerekli kutuphaneyi yukleyin.'),
                    html.P('Ilgili kutuphaneyi unuttuysaniz soldaki linkten bakabilirsiniz'),
                    html.P('Su an yaptigimiz gibi degil de sifirdan bir projeye baslasaydik ve daha once bu kutuphaneyi virtenv yuklemeseydik hata alacaktik'),
                    html.P('Ancak biz requirements.txt dosyasindaki tum ilgili kutuphaneleri daha once virtenv e yukledigimiz icin artik sorunsuzca PosstgreSQL e baglanabiliriz.'),
                    html.P('... dosyasindaki ... numarali satirlar bizim tablo olusturmamiz icin bos birakilan satirlar'),
                    html.P('Simdi teker teker ilgili tablolari olusturun, her defasinda tablonun olusup olusmadigini PostgreSQL arayuzunden kontrol edin'),
                    html.P('Eger son 3 tabloyu da olustursaniz artik tablo olusturmak icin yazdiginiz python kodlarini silebilirsiniz.'),
                    html.P('Simdi elimizde 9 tablo var ama hepsi bos'),
                    html.P('Simdi veri yukleyelim..')

                ], className='mt-3')

    elif pie == 'crud':
        return html.Div([
                    html.H3('CRUD komutlari'),
                    html.P('Veri yuklerken de tablo olustururken kullandigimiz yontemleri kullanacagiz'),
                    html.P(
                        'Yani once PostgreSQL arayuzunden manuel olarak, yine PostgreSQL arayuzunden SQL komutlariyla ve son olarak Pycharm uzerinden.'),
                    html.P('... numarali satirlar bizim veri eklememiz icin bos birakilan satirlar'),
                    html.P('bu uc yontemle 3 tabloya en az 5 er tane veri eklemeye calisin.'),
                    html.P('Her veriyi eklediginizde PostgreSQL uzerinden verinin eklenip eklenmedigini kontrol edin.'),
                    html.P('Artik veri ekleyebiliyoruz.'),
                    html.P('Simdi de bazi verileri degisitrelim'),
                    html.P('Yine 3 yontemi kullanarak en az 15 degisiklik yapalim'),
                    html.P(
                        'Simdi de silmeye baslayalim, ama tablolarimizi degil, sadece verileri yani satirlari, yine 3 yontemle...'),
                    html.P('Esasinda yukarida yaptigimiz bu islemlere CRUD islemleri denmekte yani ... basharfleri'),
                    html.P('Cok guzel, CRUD islemlerini yaptik ama ogrencegiz derken elimizde veri kalmadi'),
                    html.P('Bir sonraki bolumde devam edelim.')
                ], className='mt-3')

    elif pie == 'importt':
        return html.Div([
                    html.H3('Import edilmesi'),
                    html.P('Simdi biraz da sorgu yapalim diyecegim ama dedigim gibi elimizde ver kalmadi.'),
                    html.P('Hem elimzde veri olsa bile sadece 15 veri girebildik'),
                    html.P('Bu kadar az veriyle hem karisik sorgular yapmak zor olur hem de gercekci olmaz cunku gercek hayattaki DB tablolari milyon satirlar barindiriyor'),
                    html.P('O zaman geriye bir secenek kaliyor, verileri bir yerden yuklemek yani import etmek'),
                    html.P('Import ve export etmeyi ogrenmek onemli, cunku gercek hayatta baska bir yerde bulunan veriyi kendi DB mize cekmek isteyebiliriz,'\
                           ' ya da DB mizdeki bir veriyi bir sebeple disari aktarmak zorunda kalabiliriz.'),
                    html.P('Simdi ... reposuna gidin ve ... csv dosyasini PostgreSQL arayuzunu kullanarak import edin.'),
                    html.P('Guzel, tablolarimiz doldu, artik sorgularimizi yapabiliriz'),
                ], className='mt-3')

    elif pie =='sorgu':
        return html.Div([
                    html.H3('Sorgularin yapilmasi'),
                    html.P('Sorgular cok onemli, cunku verilerimizi DB de oylece dursunlar diye tutmuyoruz, bu veriyi kullanmamiz lazim.'),
                    html.P('Ama cok fazla veri var, ihtiyacimiz olanin uzerinde.'),
                    html.P('Ihtiyacimiz ne peki?'),
                    html.P('Ihtiyaclarimiz cok degisken, bu sirkette kac personel calisiyordan tutun da gecen sene ise giren ve X Bolgesinde en fazla satis yapan elemani bulmaya kadar gidiyor.'),
                    html.P('Yani elimizdeki veriyi bir sekilde yararli hale getirmemiz lazim, bunu yolu da sorgular'),
                    html.P('Daha fazla edebiyat yapmayalim, cunku sorgularin ne oldugunu zaten biliyorsunuz.'),
                    html.P('Sorgulari 2 yontemle yapacagiz: PostgreSQL uzerinden ve Pycharm uzerinden'),
                    html.P('Asagidaki sorularin yanitlarini verecek sorgulari ayri ayri 2 yontemle de yapmaya calisin.'),
                    html.P('Sorgularinizi gerceklestirdikten sonra silmeyin SQL ve python kodlarini hersoru icin altalta bir dosyaya yapistirin.'),
                    html.P('Dosyanin en ustune daha once yaptigimiz DB olusturma, tablo olusturma ve CRUD komutlarini da ekleyin.'),
                    html.P('Dosyanin en altina da gectigimiz 3 hafta boyunca yararlandiginiz linkleri ekleyin.'),
                    html.P('Ilerde SQL denince basvurabilecegimiz ve icinde ornekler iceren guzel bir document yaptik.'),
                    html.P('Ve tabiki bu documenti github ... reposuna yukleyin. Kolay yoldan, file upload ederek :)'),
                    html.H4('Cevaplanacak sorular'),
                    html.P('Kac çeşitler urun üretiliyor?'),
                    html.P('calisanlarin yüzde kaçı kadin?'),
                    html.P('hem calisan hem de müşteri olanlar kimler?'),
                    html.P('bolgelere gore ciro dagilimi nasil?'),
                    html.P('...'),
                    html.P('...'),
                    html.P('...'),
                    html.P('...'),
            ], className='mt-3')

    elif pie == 'exportt':
        return html.Div([
                    html.H3('Export edilmesi'),
                    html.P('Export un da onemli oldugunu soylemistik.'),
                    html.P('O zaman ufak bir export islemi yapalim da bunu da ogrenmedik demeyelim.'),
                    html.P('.... sorgusunu yapin ve cikan sonuc tablosunu export edin.'),
                    html.P('Ve csv dosyasini tabiki github ... reposuna yukleyin, bu sefer kolay yoldan degil, coder gibi yani terminal kullanarak :)')
                ], className='mt-3')

    elif pie == 'dashboard':
        return html.Div(['Welcome to dashboard page'])

    elif pie == 'sonuc':
        return html.Div([
                    html.H3('Sonuc'),
                    html.P('Oncelikle Tebrikler...'),
                    html.P('Buraya gelene kadar guzel is cikardik.'),
                    html.P('Eger projenin tum asamalarini yaptiysaniz iyi yol kattetiniz demektir.'),
                    html.P('Artik ilk is gunu bilgisayarin basina gectiginizde heyecanlanmaniza gerek yok. DB konusunda en azindan... '),
                    html.P('Su ana kadar neler yaptigimizi bir gozden gecirirsek;'),
                    html.U([
                        html.Li('Her sekilde DB ye baglandik'),
                        html.Li('CRUD yaptik'),
                        html.Li('Veri cektik, veri ekledik'),
                        html.Li('Bircok sorgu yaptik'),
                        html.Li('Kendi capimizda basvurabilecegimiz bir document yaptik'),
                        html.Li('Baskasinin reposunu fork ettik'),
                        html.Li('Github reposuna odev gonderdik'),
                        html.Li('ve oldukca modern gorunen guzel bir dashboard yaptik')
                    ]),
                    html.P('Ama yapacaklarimiz daha bitmedi, cunku icimize sinmeyen birseyler var'),
                    html.P('Bu is icin cok emek verdik, kimsenin arayuzunu goremedigi, githubdan sadece kodlarini gordugu bir proje olsun istemiyoruz.'),
                    html.P('O zaman bunu internete yuklemeliyiz ki herkes gorebilsin'),
                    html.P('...'),
                    html.P("..."),
                    html.P("..."),
                    html.P('Ve iste bu kadar.. Herkesin gorebildigi, githubinizda gururla gosterebileceginiz, CV nize link verebileceginiz guzel bir proje'),
                    html.P('Data Science kisminda gorusmek uzere :)')
                ], className='mt-3')


    else:
        return html.Div([
                    html.H1('SQL projesine hosgeldiniz...'),
                    html.H3('Neler ogrendik?'),
                    html.U([
                        html.Li('DB nedir? DB cesitleri nelerdir?'),
                        html.Li('DB nasil olusturulur?'),
                        html.Li('Table relations semasi nasil kurulur?'),
                        html.Li('SQL-NoSQL?'),
                        html.Li('Query komutlari nelerdir?'),
                        html.Li('PosrgreSQL'),
                        html.Li('Mongo DB'),
                    ]),
                    html.P(''),
                    html.P('Bu proje ile gectigimiz 3 hafta boyunca gordugumuz konulari pekistirecegiz.'),
                    html.P('Projemizi 2. hafta gordugumuz PostgreSQL kullanarak gerceklestirecegiz.'),
                    html.P("Projede kulanacagimiz veri ise 'Northwind sample database' verisi olacak."),
                    html.P('Ayrica arayuz tasariminda ise Plotly.Dash kutuphaensini kullanacagiz.'),
                    html.P(
                        'Projedeki asil gayemiz, bir database tum yollardan ulasmaya calismak ve istedigimiz islemleri uygulamak'),
                    html.P('Bunun icin projemizi yaparken 3 yol kullanacagiz.'),
                    html.P(
                        'Ilk olarak PostgreSQL in arayuzunu kullanarak tablo olusturacak ve sorgularimizi gerceklestirecegiz.'),
                    html.P('Sonrasinda Pycharm gibi bir IDE uzerinden ayni islemleri gerceklestirecegiz'),
                    html.P(
                        'Son olarak ise baska bir arayuz uzerinden buttonlara kendimiz fonksiyonellik kazandirarak ayni islemleri yapacagiz'),
                    html.P('Bu, ayni zamanda user olarak bir tusa bastigimizda arka planda neler oldugunu gormemizi saglayacak'),
                    html.P('Okuyunca havali geliyor degil mi?'),
                    html.P('Gercekte de havali :)'),
                    html.P('Eger bu projeyi istenilen sekilde yaparsaniz github hesabiniza yukleyebileceginiz ve CV nizde rahatlikla gosterebileceginiz guzel bir projeniz olmus olacak.'),
                    html.P('Sizi daha fazla heyecanlandirmadan hadi baslayalim'),
                    html.P(''),
                ],className='mt-3')


# @app.callback(
#     Output("modal-centered", "is_open"),
#     [Input("open-centered", "n_clicks"),
#      Input("close-centered", "n_clicks")],
#     [State("modal-centered", "is_open")],
# )
# def toggle_modal(n1, n2, is_open):
#     if n1 or n2:
#         return not is_open
#     return is_open



# @app.callback(
#     Output("relations-diagram", "childeren"),
#     [Input("open-centered", "n_clicks")]
# )
# def click_button(n_click):
#
#     if not n_click == None:
#         return html.Div(html.Img(src='/assets/relations schema.png', height='750', width='750'))
#     else:
#         ''



if __name__ == '__main__':
    app.run_server(debug=True)