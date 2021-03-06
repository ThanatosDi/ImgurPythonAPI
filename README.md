# ImgurPythonlibrary

## 安裝
   * 安裝必要套件  
    `python -m pip install -r requirements.txt`  
    
   * 匯入library  
    `from ImgurPythonlibrary.Imgur import Imgur`
## 使用
當操作不需要認證時 refresh_token 可以保持為空，但需要認證的操作就需要 refresh_token  
* 不需認證
```python
client_id = '123456789'
client_secret = '123456789asdzxcqwe123456'
Client = Imgur(client_id, client_secret)
Data = Client.Album('EPGUzgm')
print(Data)
```
* 需要認證
```python
client_id = '123456789'
client_secret = '123456789asdzxcqwe123456'
refresh_token = '5648444sd8g4sd8g445asf88awf44'
Client = Imgur(client_id, client_secret, refresh_token)
Data = Client.Account('username')
print(Data)
```
## Functions
* 帳號 Account
* [x] Generate Access Token
* [x] Account Base
* [x] Account Block Status
* [x] Account Blocks
* [x] Account Block Delete
* [x] Account Images
* [x] Account Gallery Favorites
* [x] Account Favorites
* [x] Account Submissions
* [ ] ~~Account Delete~~  
* 相片簿(專輯) Album  
* [x] Album
* [x] Album Images
* [x] Album Images Detail
* 圖片 Image
* [x] Image
* [x] Image Upload
* [x] Image Delete
* [x] Update Image Information
* 其他 Else
* [x] binaryfile

目前還尚未完成，現階段只完成部分功能，一般回傳格式為 dict  

  *  ### 帳號 Account
     *  #### Get_token()
          不需驗證  
          取得 refresh_token，回傳網址請在瀏覽器開啟
     *  #### Refresh_token()
          需驗證  
          重新取得 access_token(一個月後過期) 及 refresh_token(據說不會過期)
     *  #### Account('username')
          不需驗證  
          取得 username 帳號資料
     *  #### Account_Block_Status('username')
          不需驗證  
          取得 username 帳號封鎖狀態
     *  #### Account_Blocks('username')
          需驗證  
          取得 username 封鎖列表
     *  #### Account_Images()
          需驗證  
          取得帳號的圖片
     *  #### Account_Block_Create('username')
          需驗證  
          封鎖一個使用者
     *  #### Account_Block_Delete('username')
          需驗證  
          解除封鎖一個使用者
     *  #### Account_Gallery_Favorites('username', page:int , sort:str='newest')
          不需驗證  
          取得用戶在圖庫中收藏的圖像  
          (Optional)  
           * page
              integer - allows you to set the page number so you don't have to retrieve all the data at once.
           * sort
               `oldest`, or `newest`. Defaults to `newest`.
     *  #### Account_Favorites('username', page: int , sort: str = 'newest')
          需驗證
          取得用戶收藏的圖像
          (Optional)
           * page
              integer - allows you to set the page number so you don't have to retrieve all the data at once.
           * sort
               `oldest`, or `newest`. Defaults to `newest`.
     *  #### Account_Submissions('username', page: int , sort: str = 'newest')
          不需驗證  
          取得用戶已提交到圖庫的圖像
          (Optional)
           * page
              integer - allows you to set the page number so you don't have to retrieve all the data at once.
           * sort
               `oldest`, or `newest`. Defaults to `newest`.
  *  ### 評論 Comment
  *  ### 相片簿(專輯) Album
     *  #### Album('album_id')
          不需驗證  
          取得相片簿(專輯)的資料
     *  #### Album_Images('album_id',image_id:str)
          不需驗證  
          取得相片簿(專輯)的圖片資料，如果有image_id則回傳該圖片的資料
  *  ### 畫廊 Gallery
  *  ### 圖片 Image
       *  #### Image_Upload(image, auth=False, Optional)
          不需驗證 auth=False、需驗證 auth=True  
          上傳圖片  
          (Optional)  
             * album  
                The id of the album you want to add the image to.
             * type  
                file, base64 or URL.
             * name  
                The name of the file.
             * title  
                The title of the image.
             * description  
                The description of the image.
       *  #### Image_Delete(image(id or deleteHash), auth=False)
          不需驗證 auth=False、需驗證 auth=True  
          不需驗證需要 deleteHash 有驗證只需要 image id即可  
          刪除指定圖片
