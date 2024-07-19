from flask import Flask, render_template, make_response
from flask_cors import CORS
import sqlite3
import re
app = Flask(__name__)
CORS(app)

def get_db_connection():
   conn = sqlite3.connect('data.db')
   return conn

@app.route('/rank/<param>', methods=['POST', 'GET'])
def hello(param):
   app.logger.debug(f"GET: {param}")
   conn = get_db_connection()
   cur = conn.cursor()
   cond = re.compile(r"\d{6}")
   if not re.fullmatch(cond, param):
      html = '<p class="text-danger">Vui lòng nhập số báo danh hợp lệ!</p>'
      return html
   scores = cur.execute(f'SELECT * FROM scores WHERE scores.ID = {param};').fetchall()
   app.logger.debug(f"GOT IN DB: {scores}")
   conn.close()

   if scores:
      data = scores[0]
      rank = data[6]
      status = 'success' if rank <= 564 else 'warning'
      status_text = 'Trúng tuyển' if rank <= 564 else 'Chờ xử lý'
      html = f"""
      <tr>
         <td>{data[0]}</td>
         <td>{data[1]}</td>
         <td>{data[2]}</td>
         <td>{data[3]}</td>
         <td>{data[4]}</td>
         <td>{data[5]}</td>
         <td>{data[6]}</td>
         <td><span class="badge bg-{status}">{status_text}</span></td>
      """
      return make_response(html, 200)
   
   html = '<p class="text-warning">Không tìm thấy kết quả</p>'
   return html