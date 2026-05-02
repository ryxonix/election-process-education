from flask import Blueprint, render_template, request
from core.election_logic import ElectionLogicEngine
from core.guardrails import SemanticInterceptor

# Initialize Blueprint and Core Engines
api_bp = Blueprint('api', __name__, template_folder='../ui/templates')
logic_engine = ElectionLogicEngine()
interceptor = SemanticInterceptor()

@api_bp.route('/')
def index():
    return render_template('index.html')

@api_bp.route('/registration')
def registration():
    return render_template('registration.html')

@api_bp.route('/verification')
def verification():
    return render_template('verification.html')

@api_bp.route('/polling')
def polling():
    return render_template('polling.html')

@api_bp.route('/simulator', methods=['GET', 'POST'])
def simulator():
    scenario_data = None
    override_msg = None
    
    if request.method == 'POST':
        issue = request.form.get('issue')
        custom_query = request.form.get('custom_query', '')
        
        # Guardrail Check: Intercept custom queries for partisan logic
        sanitization_result = interceptor.sanitize(custom_query)
        if not sanitization_result['is_safe']:
            override_msg = sanitization_result['override_message']
            # Default to normal flow if an adversarial injection is detected
            scenario_data = logic_engine.evaluate_scenario('normal')
        else:
            # Safe evaluation via Chain-of-Thought engine
            scenario_data = logic_engine.evaluate_scenario(issue)

    return render_template('simulator.html', scenario_data=scenario_data, override_msg=override_msg)
