# Pico y Placa Predictor

### 👩🏻‍💻 Project Overview

This project is a Pico y Placa Predictor implemented using FastAPI for the backend and Streamlit for the frontend. It determines whether a vehicle can be on the road based on the license plate number, date, and time, following Quito's Pico y Placa regulations.

The project follows a clean architecture with an object-oriented programming (OOP) approach, ensuring modularity, maintainability, and scalability.

### 📁 Project Structure
<img src="https://github.com/user-attachments/assets/44336ac2-90af-4933-8b32-1bfd713ee660" alt="Descripción" width="500" height="400">

### ⚙️ Installation & Setup

**1. Clone the repository**

      git clone https://github.com/KeylaMunnoz/pico_y_placa_predictor.git
      cd pico_y_placa_predictor_py

**2. Create and activate a virtual environment**

      python -m venv venv
      source venv/bin/activate  # On macOS/Linux
      venv\Scripts\activate  # On Windows
    
**3. Install dependencies**
   ```bash
    pip install -r requirements.txt
   ```

**4. Run the FastAPI backend**
   ```bash
    uvicorn app.main:app --reload
   ```
   - The API will be available at: http://127.0.0.1:8000
   - API documentation (Swagger UI): http://127.0.0.1:8000/docs
     
**5. Run the Streamlit frontend**
   ```bash
    cd frontend
    streamlit run frontend.py
   ```
   - The frontend UI is deployed at: https://pico-y-placa.streamlit.app/


### ✅ Running Tests
   ```bash
    pytest tests/
   ```

### 📜 API Endpoints
| Method | Endpoint | Description |
|-----------|-----------|-----------|
| POST | /predictor/check | Checks if a car can be on the road |


**Example Request (JSON):**
  ```json
  {
    "plate_number": "ABC-1234",
    "date": "2025-02-28",
    "time": "10:00"
  }
  ```
**Example Response:**
  ```json
  {
    "can_drive": true,
    "message": "Your car can be on road"
  }
  ```

### 📌 License Plate Validation
- The Ecuadorian plate format: ABC-1234 or ABC-123
- Only valid province letters are allowed

  Information was consulted from: https://ecuadorec.com/placas-vehiculos-ecuador-tipos-letras-provincia/
  
### 📆 Pico y Placa Rules
| Last Digit | Restricted Day | 
|-----------|-----------|
| 1,2 | Monday |
| 3,4 | Tuesday |
| 5,6 | Wednesday |
| 7,8 | Thursday |
| 9,0 | Friday |

**⏰ Restricted hours:**
- Morning: 07:00 - 09:30
- Evening: 16:00 - 19:30

Information was consulted from: https://www7.quito.gob.ec/mdmq_ordenanzas/Administraci%C3%B3n%202019-2023/Sesiones%20de%20Concejo/2019/Sesi%C3%B3n%20Ordinaria%202019-09-03/V.%20Plan%20Hoy%20no%20Circula/Informe%20-%20Hoy%20no%20circula.pdf
